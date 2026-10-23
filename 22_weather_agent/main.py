from openai import OpenAI # type: ignore[reportMissingImports]
from dotenv import load_dotenv # type: ignore[reportMissingImports]
import os
import requests  # type: ignore[reportMissingImports]

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    return "Could not retrieve weather information."


def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-3.8-flash",
        messages=[
            {
                "role": "user",
                "content": user_query,
            }
        ],
    )

    print(response.choices[0].message.content)


main()
print(get_weather("goa"))