Docs

## Getting Started

Set up LGTM in under 5 minutes and get your first AI-powered code review.

Quick Setup

1

Sign in with GitHub

Click 'Sign in with GitHub' on the login page. LGTM uses GitHub OAuth to authenticate your account. We only request the permissions needed to read your repos and post reviews.

2

Add your AI API key

Go to Settings and add an API key for OpenAI or Google Gemini. This is your own key (BYOK) — LGTM never stores or shares it beyond making review calls on your behalf.

3

Connect a repository

Head to the Repos page and click 'Connect Repo'. Select any repository where the LGTM GitHub App is installed. The app automatically configures webhooks for you.

4

Get your first review

Open or update a pull request on your connected repo. If auto-review is enabled, LGTM will automatically analyze the PR and post a detailed review with inline comments directly on GitHub.

Key Concepts

BYOK (Bring Your Own Key)

You provide your own API keys for AI providers. Your code is sent directly to the AI provider and never stored on our servers beyond the review session.

Multi-Agent Review

Every PR is analyzed by 6 specialist AI agents in parallel, each focused on a different aspect. A synthesizer then combines their findings into one cohesive review.

Context-Aware

LGTM indexes your codebase using tree-sitter and PageRank to understand your project structure. Reviews include relevant context from related files, not just the diff.

Real-time Updates

Watch reviews happen live in the dashboard. Socket-based events show each agent's progress, findings, and the final synthesized verdict as it happens.