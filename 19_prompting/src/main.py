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
            "role": "system",
            "content":"You are expert in Maths and only and only ans maths related questions. If the question is not related to maths, answer with 'I am sorry, I can only answer maths related questions.'"

        },
        {
            "role": "user",
            "content": "2 + 2"
        }
    ]
)

print(response.choices[0].message.content)