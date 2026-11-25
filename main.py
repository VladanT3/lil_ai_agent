import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY env was not found.")

parser = argparse.ArgumentParser(description="lil ai bot")
parser.add_argument("prompt", type=str, help="The prompt to run.")
args = parser.parse_args()

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.prompt
        }
    ]
)
if response.usage is not None:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)
