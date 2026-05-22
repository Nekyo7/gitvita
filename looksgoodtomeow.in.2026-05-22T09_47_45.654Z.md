![LGTM](https://looksgoodtomeow.in/logo.png)Looks Good To Meowv1.0.0 — Beta

# AI code reviewsthat actually understand your codebase.

6 specialist agents run in parallel on every PR — security, bugs, performance, readability, best practices, and docs. A synthesizer weighs all findings and posts the verdict as a GitHub review.

Connect your reposConnect your reposRead Docs

app.lgtm.dev/review/pr-42

feat: add OAuth login flow

PR #42 into main

Changes

Agent Pipeline

6/8 complete

Context Indexer

Indexed 847 files via tree-sitter

Security

2 critical findings

Bugs

1 logic error found

Performance

1 N+1 query detected

Readability

1 suggestion

Best Practices

All good

Documentation

Analyzing...

Synthesizer

Waiting for agents...

Inline Comments

critical · auth.ts:42

SQL injection — use parameterized queries

perf · user.service.ts:88

N+1 query — batch with $in operator

Review progress57%

< 3 min

Review time

6 + 1

Agents + Synthesizer

OWASP

Top 10 covered

BYOK

Your keys, your data

Features

## Everything for  automated review

Deep analysis, not shallow linting. Built for maintainers who want reliable first-pass reviews they can trust.

### 6 + 1 Agent Architecture

Security, bugs, performance, readability, best practices, and documentation agents run in parallel. A synthesizer weighs all findings and posts the final verdict.

Layer 1

Context

Layer 2

6 Specialists

Layer 3

Synthesizer

### Full Repo Context

LGTM indexes your codebase with tree-sitter — builds a dependency graph, extracts conventions, and summarizes recent history. Reviews understand your code, not just the diff.

### Under 3 Minutes

All specialist agents run in parallel. From PR opened to review posted with inline comments — faster than your CI.

### Bring Your Own Keys

OpenAI or Gemini — add your API keys, pick your model. Override per-repo if you want. Anthropic support coming soon.

### GitHub Native

Reviews posted as PR comments with inline code suggestions. Approve or request changes from the dashboard.

### Smart Notifications

In-app and email alerts for completed reviews, AI approvals, and critical security findings.

### Contributor Dashboard

Open a PR on any connected repo and sign in to see all your AI reviews in one place — with verdicts, findings, and confidence scores.

Architecture

## 6 specialists. 1 synthesizer.  One senior-level review.

Each agent is a specialist. They run in parallel, then a synthesizer weighs all findings and posts the final verdict — like a senior engineer would.

Layer 1

Runs on push to main

### Context Indexer

Parses your repo with tree-sitter across 12 languages, builds a dependency graph with PageRank, extracts coding conventions, and summarizes recent PR history. Runs on every push to your default branch.

Layer 2

6 specialists in parallel on every PR

#### Security

OWASP Top 10, secrets, injection, XSS, SSRF

#### Bugs

Logic errors, null refs, race conditions

#### Performance

N+1 queries, complexity, re-renders

#### Readability

Naming, structure, complexity, clarity

#### Best Practices

Patterns, error handling, conventions

#### Documentation

Missing docs, outdated comments, JSDoc

Layer 3

Synthesizer after all specialists complete

### Synthesizer

Consumes all 6 reports + repo context. Weighs findings, resolves conflicts, generates a changelog entry, and posts the final verdict with inline comments on your PR.Approve, request changes, or comment.

How it works

## From PR to review  in 4 steps

01

### Connect your repo

Sign in with GitHub, add your AI provider API key, and connect any repo in two clicks. Webhooks installed automatically.

02

### Open a pull request

Push code and open a PR as you normally would. LGTM picks it up instantly via webhook — no config, no CLI.

03

### Agents analyze in parallel

Security, bugs, performance, readability, best practices, and documentation agents all run simultaneously with full repo context. Then a synthesizer weighs all findings.

04

### Get your review

A synthesized review is posted as a GitHub comment with inline suggestions. Full report on the LGTM dashboard.

Review Complete

Here's what a finished LGTM review looks like — posted directly on your PR.

github.com/acme/api/pull/42

### feat: add OAuth login flow with JWT refresh

PR #42 by @developer into main· reviewed in 2m 14s

Request Changes

91% confidence

6 agents + synthesizer done

6

Findings

2

Critical

14

Files reviewed

5

Inline comments

Security

2 findings

Bugs

1 finding

Performance

1 finding

Readability

1 finding

Best Practices

1 finding

Documentation

0 findings

Final Verdict — Synthesizer

2 critical security issues must be fixed before merge. The login endpoint at`src/routes/auth.ts:42`accepts unsanitized input vulnerable to injection. Token refresh logic has no test coverage for edge cases. One N+1 query in the user service needs batching. Documentation is up to date. Changelog has been auto-drafted.

5 inline comments posted on GitHub

auth.ts:42— SQL injection — use parameterized queries

auth.ts:67— JWT secret loaded from env without fallback

user.service.ts:88— N+1 query — batch with $in operator

auth.test.ts:1— Missing tests for refresh token rotation

auth.controller.ts:23— Add rate limiting to login endpoint

Bring your own API key. Pick your model. Override per-repo.

OpenAI

GPT-4o, o1, o3-mini

Google

Gemini 2.5 Pro, Flash

Anthropic

Coming soon

CLI

## Review before you push.  From your terminal.

Install the LGTM CLI and get AI-powered reviews on local changes — staged or unstaged — with real-time agent streaming.

~/projects/my-api

$ npm install -g @tarin/lgtm-cli

$ lgtm login

✓ Logged in as @developer

$ lgtm review --staged

Reviewing staged changes in acme/api...

Agents running:

✓ Security 2 issues(3.2s)

✓ Bugs 0 issues(2.8s)

✓ Performance 1 issue(3.5s)

✓ Readability 0 issues(2.1s)

✓ Best Practices 1 issue(2.9s)

✓ Synthesizer done(4.1s)

──────────────────────────────

Verdict: REQUEST CHANGES

Confidence: 87%

──────────────────────────────

Issues: 2 critical1 medium

@tarin/lgtm-cli

Available on npm

$npm install -g @tarin/lgtm-cli

Read the docs

Real-time streaming

Watch agents work live in your terminal

Secure auth

GitHub OAuth with auto-refreshing tokens

Local diff review

Review uncommitted or staged changes

PR review

Trigger reviews for open PRs by number

Pricing

## Simple, transparent  pricing

Start free. Upgrade when you need unlimited reviews and auto-review on every PR.

Free

Get started

₹0/month

50 reviews per month

6 AI review agents

All security checks

CLI + Dashboard access

Get Started

POPULAR

Pro

For serious devs

₹399/month

or ~399 INR/month

Unlimited reviews

Auto-review on PRs

6 AI review agents

All security checks

CLI + Dashboard access

Priority support

Upgrade to Pro

BYOK — Bring Your Own API Keys. You only pay for the AI tokens you use.

![LGTM](https://looksgoodtomeow.in/logo.png)

## Stop waiting days  for code reviews

Connect your first repo in under a minute. Your next PR gets a full AI-powered review automatically.

Get started with GitHubGet started

Your API keys stay with you. Code is read via GitHub API and never stored.