import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from your .env file

client = Anthropic()  # picks up the key automatically

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Give me 3 ideas to increase profit for a small restaurant on Nias Island, Indonesia."}
    ],
)

print(response.content[0].text)
print(f"\n--- Tokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out ---")