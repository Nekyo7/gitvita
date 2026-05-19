import logging
from analyzer.llm_client import call_llm

logger = logging.getLogger(__name__)

class AISummaryError(Exception):
    pass

def generate_deterministic_summary(commit: dict) -> str:
    author = commit.get("author", "Unknown Author")
    health = commit.get("health_score", 100.0)
    files = commit.get("files_changed", 0)
    ins = commit.get("insertions", 0)
    dels = commit.get("deletions", 0)
    msg = commit.get("message", "").strip()

    # Determine status label
    if health >= 85:
        status = "excellent health score"
    elif health >= 65:
        status = "stable baseline score"
    elif health >= 45:
        status = "moderate health score due to increased churn"
    else:
        status = "warning level score due to high complexity and churn"

    summary = f"The latest commit by {author} results in a {status} of {health:.1f}/100. "
    summary += f"This commit modified {files} file{'s' if files != 1 else ''} with {ins} insertions and {dels} deletions. "
    
    if msg:
        msg_clean = msg.split('\n')[0]
        if len(msg_clean) > 85:
            msg_clean = msg_clean[:82] + "..."
        summary += f"Development focus: '{msg_clean}'."
    else:
        summary += "No commit message was provided."
    return summary

def generate_summary(commit: dict) -> str:
    prompt = f"""Explain this repository health change.

Files changed: {commit['files_changed']}
Insertions: {commit['insertions']}
Deletions: {commit['deletions']}
Health score: {commit['health_score']}

Give a concise engineering explanation in 2-4 sentences."""

    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        reply, model_used = call_llm(messages)
        logger.info("Generated commit summary using %s.", model_used)
        return reply
    except Exception as exc:
        logger.warning("Central LLM call failed for summary: %s. Falling back to deterministic summary.", exc)
        return generate_deterministic_summary(commit)

def generate_danger_explanation(commit: dict) -> str:
    prompt = f"""Explain why this commit is labeled the "MOST DANGEROUS COMMIT" in the codebase.
    
    Commit Message: {commit.get('message', 'No message')}
    Files Changed Count: {commit.get('files_changed', 0)}
    Insertions: {commit.get('insertions', 0)}
    Deletions: {commit.get('deletions', 0)}
    Health Drop Score: {commit.get('health_drop', 0)}
    
    Provide a highly technical, sharp, and concise 1-2 sentence engineering explanation of the potential risk (e.g. bypass validation, architectural regression, cross-module coupling). Keep it punchy and realistic."""

    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        reply, model_used = call_llm(messages)
        logger.info("Generated dangerous commit explanation using %s.", model_used)
        return reply.strip()
    except Exception as exc:
        logger.warning("Central LLM call failed for danger explanation: %s. Falling back to deterministic explanation.", exc)
        return f"This commit represents a critical architectural risk due to high churn ({commit.get('insertions', 0)} insertions / {commit.get('deletions', 0)} deletions) across {commit.get('files_changed', 0)} files, potentially violating modular decoupling constraints."
