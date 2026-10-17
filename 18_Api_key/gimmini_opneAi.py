from openai import OpenAI # type: ignore[reportMissingImports]
from dotenv import load_dotenv # type: ignore[reportMissingImports]
import os

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message.content)