import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


def extract_simple_metadata(text: str) -> dict[str, int]:
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = len([s for s in text.split(".") if s.strip()])

    return {
        "char_count": char_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
    }


def extract_llm_metadata(text: str) -> dict:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    prompt = f"Extract topic, key_entities, sentiment from this text and return ONLY JSON, no other text:\n\n{text}"

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    import json

    return json.loads(response.content[0].text)
