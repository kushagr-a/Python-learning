# chain of thought.py
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

you are in expert in ai assistant in resolving user queries using chain of thought
you work on START, PLAN, and OUTPUT steps.
you need to first PLAN what needs to be done. The PLAN can be multiple steps.
once you think enough PLAN has been done, finally you can give an OUTPUT

Rules: 
- Strictly follow the output in JSON format.
- only run one step at a time.
- the sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON format:
{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

Example:
START: Hey, can u  solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN", "content": "Seems like user is intrested in solving the mathematical problem." }
PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS rule." }
PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here." }
PLAN: { "step": "PLAN", "content": "first we must miltiply 3 * 5 which is 15" }
PLAN: { "step": "PLAN", "content": "Now the equation is 2 + 15 / 10" }
PLAN: { "step": "PLAN", "content": "We must now divide 15 by 10 which is 1.5" }
PLAN: { "step": "PLAN", "content": "Now the equation is 2 + 1.5" }
PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5" }
PLAN: { "step": "PLAN", "content": "Great. we have solve and finally left with 3.5 as as the answer." }
OUTPUT: { "step": "OUTPUT", "content": "The final answer is 3.5" }


"""

print("Welcome to the Chain of Thought Assistant!")
print("\n\n\n")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }
]

user_input = input("Hey write your query: ")
message_history.append({"role": "user", "content": user_input})

while True:
    response = client.chat.completions.create(
        model="gemini-3.8-flash",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw_result = response.choices[0].message.content

    # Parse the JSON response
    result = json.loads(raw_result)

    # Add the assistant's response to the message history
    message_history.append({"role": "assistant", "content": raw_result})

    if result.get("step") == "START":
        print(f"Assistant (START): {result.get('content')}")
        continue  # Continue to the next iteration to get the PLAN step

    elif result.get("step") == "PLAN":
        print("The assistant is planning...", result.get("content"))
        continue  # Continue to the next iteration to get more PLAN steps

    elif result.get("step") == "OUTPUT":
        print(f"Assistant (OUTPUT): {result.get('content')}")
        break  # Exit the loop after OUTPUT is received

print("\n\n\n")
