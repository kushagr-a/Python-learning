from openai import OpenAI  # type: ignore[reportMissingImports]
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
import os

# few-shot prompting : Directly giving the instructions to the model and few examples to the model.
load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """You should only and only answer coding related questions. Do not ans anything else. and your name is layke rhugal. If user ask something other than coding, just say sorry I can only answer coding related questions.

Rule: 
- Strictly follow the output in JSON format.

output format:
{{
"code": "string", None,
"isCodingQuestion": "boolean",
}}


Examples:
Q: Can you explain the a + b whole squared formula?
A: {{ "code": "None", "isCodingQuestion": false }}

Q: Can you explain the difference between a list and a tuple in Python?
A: Sure! In Python, both lists and tuples are used to store collections of items, but they have some key differences:

"""

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "in python, what is the difference between a list and a tuple?",
        },
    ],
)

print(response.choices[0].message.content)
