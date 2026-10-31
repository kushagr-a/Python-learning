from openai import OpenAI  # type: ignore[reportMissingImports]
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # type: ignore[reportMissingImports]
from langchain_qdrant import QdrantVectorStore  # type: ignore[reportMissingImports]

import os

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Gemini embeddings or vector embeddings
base_embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# vector database connection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=base_embeddings,
)



def process_query(query: str):
    print("Seaching chunks", query)
    search_results = vector_db.similarity_search(query=query)

    context = "\n\n\n".join(
        [
            f"Page Content: {result.page_content} "
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
                "content": query,
            },
        ]
    )

    return openai_response.choices[0].message.content