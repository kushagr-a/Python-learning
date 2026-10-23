# chain of thought.py
from openai import OpenAI  # type: ignore[reportMissingImports]
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
import os
import json
import requests  # type: ignore[reportMissingImports]

# few-shot prompting : Directly giving the instructions to the model and few examples to the model.
load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"

    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    else:
        return "Could not retrieve weather information."


available_tools = {
    "get_weather": get_weather
}


SYSTEM_PROMPT = """

you are in expert in ai assistant in resolving user queries using chain of thought
you work on START, PLAN, and OUTPUT steps.
you need to first PLAN what needs to be done. The PLAN can be multiple steps.
once you think enough PLAN has been done, finally you can give an OUTPUT
You can also call a tool if required from the list of available tools.

Rules: 
- Strictly follow the output in JSON format.
- only run one step at a time.
- the sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
- if a tool is needed, use the "Tool" step.

Output JSON format:
{ "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

Available tools:
- get_weather(city: str): Take city name as input and return the current weather information for that city.

Example 1:

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


Example 2:

START: Hey, can u tell me the weather of Delhi?

PLAN: { "step": "PLAN", "content": "Seems like the user is interested in knowing the current weather in Delhi." }
PLAN: { "step": "PLAN", "content": "Looking at the request, we should use the get_weather tool with Delhi as the city." }
PLAN: { "step": "PLAN", "content": "After getting the weather data, we should summarize it in simple and understandable language." }

OUTPUT: { "step": "OUTPUT", "content": "The current weather in Delhi is [weather information returned by the tool]." }
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
    parsed_result = json.loads(raw_result)

    # Add the assistant's response to the message history
    message_history.append({"role": "assistant", "content": raw_result})

    if parsed_result.get("step") == "START":
        print(f"Assistant (START): {parsed_result.get('content')}")
        message_history.append(
            {"role": "user", "content": "Continue with the next step."}
        )
        continue  # Continue to the next iteration to get the PLAN step

    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"Assistant (TOOL): {parsed_result.get('content')}")

        if tool_to_call not in available_tools:
            raise ValueError(f"Unknown tool requested: {tool_to_call}")
        if not isinstance(tool_input, str) or not tool_input.strip():
            raise ValueError("The tool input must be a non-empty city name.")

        tool_response = available_tools[tool_to_call](tool_input)
        message_history.append(
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "step": "TOOL",
                        "content": tool_response,
                        "tool": tool_to_call,
                        "input": tool_input,
                        "output": tool_response,
                    }
                ),
            }
        )
        continue  # Continue to the next iteration to get the next step after TOOL



    elif parsed_result.get("step") == "PLAN":
        print("The assistant is planning...", parsed_result.get("content"))
        message_history.append(
            {"role": "user", "content": "Continue with the next step."}
        )
        continue  # Continue to the next iteration to get more PLAN steps

    elif parsed_result.get("step") == "OUTPUT":
        print(f"Assistant (OUTPUT): {parsed_result.get('content')}")
        break  # Exit the loop after OUTPUT is received

print("\n\n\n")
