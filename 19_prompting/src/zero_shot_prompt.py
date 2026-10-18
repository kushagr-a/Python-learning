from openai import OpenAI  # type: ignore[reportMissingImports]
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
import os

# Zero-shot prompting : Directly giving the instructions to the model without any examples.
load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = "You should only and only answer coding related questions. Do not ans anything else. and your name is layke rhugal. If user ask something other than coding, just say sorry I can only answer coding related questions."

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "your name is?"},
    ],
)

print(response.choices[0].message.content)
