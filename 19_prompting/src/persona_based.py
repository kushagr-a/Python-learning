# Persona Base Prompting --> means clone some one, make your ai talk to some one tone

from openai import OpenAI  # type: ignore[reportMissingImports]
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
import os
import json

# few-shot prompting : Directly giving the instructions to the model and few examples to the model.
load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """

You are ai persona assistant named kushagra bharti.
you are acting on bhalf of kushagra bharti who will be 22 years old and is a software engineer.
your main tech stack is js, node.js, python and leraning gen  ai and llm models.

Example:
Q: Hey
A: Hey, Kya re bhidu!


"""

# atleast give 100 - 150 examples to the model to learn the persona of the person.

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey there!!"},
    ],
)

print("Assistant:", response.choices[0].message.content)