import os
from pathlib import Path
from dotenv import load_dotenv # type: ignore[reportMissingImports]

from langchain_community.document_loaders import PyPDFLoader  # type: ignore[reportMissingImports]
from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore[reportMissingImports]
from langchain_google_genai import GoogleGenerativeAIEmbeddings # type: ignore[reportMissingImports]
from langchain_qdrant import QdrantVectorStore # type: ignore[reportMissingImports]

# Gemini api key
load_dotenv()  # Load environment variables from .env file

# Load PDF
pdf_path = Path(__file__).parent / "Nodejs.pdf"

# load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# Store human-readable, one-based page numbers in every document chunk.
for document in docs:
    document.metadata["page_number"] = document.metadata["page"] + 1

# print(f"Total pages: {len(docs)}")

# split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)

chunks = text_splitter.split_documents(docs)

# Vector embedding for the chunks
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

print("Indexing completed. You can now use the vector store for retrieval and question answering.")