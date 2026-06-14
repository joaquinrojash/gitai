import anthropic
from gitai.config import ANTHROPIC_API_KEY, MODEL, COMMIT_PROMPT, PR_PROMPT

def get_client():
    if not ANTHROPIC_API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY not set. "
            "Run: export ANTHROPIC_API_KEY='your-key-here'"
        )
    return anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_commit_message(diff: str) -> str:
    client = get_client()
    prompt = COMMIT_PROMPT.format(diff=diff)
    message = client.messages.create(
        model=MODEL,
        max_tokens=150,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text.strip()

def generate_pr_description(diff: str) -> str:
    client = get_client()
    prompt = PR_PROMPT.format(diff=diff)
    message = client.messages.create(
        model=MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text.strip()