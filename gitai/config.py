import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-sonnet-4-6"
MAX_DIFF_CHARS = 8000

COMMIT_PROMPT = """You are an expert software engineer writing git commit messages.
Given a git diff, write ONE commit message following Conventional Commits format.

Rules:
- Format: type(scope): description
- Types: feat, fix, docs, style, refactor, test, chore
- Description: lowercase, present tense, max 72 chars
- No period at the end
- Only output the commit message. Nothing else.

Git diff:
{diff}"""

PR_PROMPT = """You are an expert software engineer writing GitHub Pull Request descriptions.
Given a git diff, write a clear PR description in markdown.

Include:
- A one-sentence summary
- What changed and why (bullet points)
- Any important notes for reviewers

Git diff:
{diff}"""