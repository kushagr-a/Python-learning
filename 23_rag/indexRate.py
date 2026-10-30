
import os
import time
from pathlib import Path
from dotenv import load_dotenv # type: ignore[reportMissingImports]

from langchain_community.document_loaders import PyPDFLoader # type: ignore[reportMissingImports]
from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore[reportMissingImports]
from langchain_google_genai import GoogleGenerativeAIEmbeddings # type: ignore[reportMissingImports]
from langchain_qdrant import QdrantVectorStore # type: ignore[reportMissingImports]
from langchain_core.embeddings import Embeddings # type: ignore[reportMissingImports]

load_dotenv()

# Load PDF
pdf_path = Path(__file__).parent / "Nodejs.pdf"

loader = PyPDFLoader(file_path=str(pdf_path))
docs = loader.load()

print(f"Total pages: {len(docs)}")

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")


# Gemini embeddings
base_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


# Rate-limited embedding wrapper
class RateLimitedEmbeddings(Embeddings):

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def embed_documents(self, texts):

        all_vectors = []
        batch_size = 10

        for i in range(0, len(texts), batch_size):

            batch = texts[i:i + batch_size]

            for attempt in range(3):
                try:
                    vectors = self.embeddings.embed_documents(
                        batch,
                        batch_size=batch_size
                    )

                    all_vectors.extend(vectors)
                    break

                except Exception as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        print("Rate limit reached. Waiting 25 seconds...")
                        time.sleep(25)
                    else:
                        raise

                    if attempt == 2:
                        raise

            print(f"Embedded {len(all_vectors)}/{len(texts)} chunks")

            time.sleep(2)

        return all_vectors

    def embed_query(self, text):
        return self.embeddings.embed_query(text)


embeddings = RateLimitedEmbeddings(base_embeddings)


# Store vectors in Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
    batch_size=10
)

print("Indexing completed successfully!")
