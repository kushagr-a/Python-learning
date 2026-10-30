# Here Retrival code
import os

from dotenv import load_dotenv # type: ignore[reportMissingImports]
from openai import OpenAI # type: ignore[reportMissingImports]

from langchain_google_genai import GoogleGenerativeAIEmbeddings # type: ignore[reportMissingImports]
from langchain_qdrant import QdrantVectorStore # type: ignore[reportMissingImports]

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Gemini embeddings
base_embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=base_embeddings,
)

# Take user input
user_Query = input("Enter your query: ")

# simalarity search return relevant chuks based on the user query
search_results = vector_db.similarity_search(user_Query)


def get_page_number(metadata: dict) -> int | str:
    page_number = metadata.get("page_number")
    if page_number is not None:
        return page_number

    page = metadata.get("page")
    return page + 1 if isinstance(page, int) else "N/A"


context = "\n\n\n".join(
    [
        f"Page Content: {result.page_content} "
        f"(Page Number: {get_page_number(result.metadata)})"
        for result in search_results
    ]
)

SYSTEM_PROMPT = """
You are a helpful assistant that answers questions using only the provided context.
For every factual statement, include its source page in the format "(Page Number: X)".
Use the page number attached to the relevant context item. Never use "N/A" when a
page number is available. If multiple pages support an answer, cite each page.
If the context does not contain the answer, respond exactly with "I don't know."

Context:
{context}
"""

openai_response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT.format(context=context),
        },
        {
            "role": "user",
            "content": user_Query,
        },
    ],
)

print("Answer:", openai_response.choices[0].message.content)