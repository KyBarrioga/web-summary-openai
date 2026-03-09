import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scraper import fetch_website_contents

SYSTEM_PROMPT = """
You are an aggressive filipino that has talks with very strong words. You are a highly sarcastic and unserious.
You don't give the accurate information but put a lot of weird information into it.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

USER_PROMPT_PREFIX = """
Here is the website for ABS CBN news channel for celebrity section. Can you give me a summary of what are the headlines here.
"""

DEFAULT_WEBSITE = "https://www.abs-cbn.com/entertainment/showbiz/celebrities"


def validate_api_key() -> str:
    load_dotenv(override=True)
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "No API key was found. Set OPENAI_API_KEY in your environment or .env file."
        )
    if not api_key.startswith("sk-proj-"):
        raise RuntimeError(
            "OPENAI_API_KEY was found, but it does not start with 'sk-proj-'."
        )
    if api_key.strip() != api_key:
        raise RuntimeError(
            "OPENAI_API_KEY contains leading/trailing whitespace. Remove extra spaces."
        )
    return api_key


def messages_for(website_text: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_PREFIX + "\n\n" + website_text},
    ]


def summarize(url: str, model: str = "gpt-4.1-nano") -> str:
    try:
        from openai import OpenAI
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Missing dependency 'openai'. Install it with: pip install openai"
        ) from exc

    website_text = fetch_website_contents(url)
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=messages_for(website_text),
    )
    return response.choices[0].message.content or ""


def main() -> int:
    #Creates a parameter for accepting url
    parser = argparse.ArgumentParser(description="Summarize a website with OpenAI.")
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_WEBSITE,
        help=f"Website URL to summarize (default: {DEFAULT_WEBSITE})",
    )
    #Accepts another parameter to accept model from openAI
    parser.add_argument(
        "--model",
        default="gpt-4.1-nano",
        help="OpenAI model name (default: gpt-4.1-nano)",
    )
    args = parser.parse_args()

    try:
        validate_api_key()
        print(summarize(args.url, model=args.model))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
