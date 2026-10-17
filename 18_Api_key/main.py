from dotenv import load_dotenv  # type: ignore[reportMissingImports]
from google import genai
import os

load_dotenv()  # Load environment variables from .env file

client = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY")
)  # Initialize the GenAI client using the API key from the environment variable

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Hey Kushagra Here!"
)

print(response.text)  # Print the generated content from the model
