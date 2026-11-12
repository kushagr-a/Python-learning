from dotenv import load_dotenv # type: ignore[reportMissingImports]
load_dotenv()  # Load environment variables from .

from typing import Annotated
from typing_extensions import TypedDict # type: ignore[reportMissingImports]
from langgraph.graph import START, END, StateGraph # type: ignore[reportMissingImports]
from langgraph.graph.message import add_messages # type: ignore[reportMissingImports]
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage # type: ignore[reportMissingImports]
from openai import OpenAI # type: ignore[reportMissingImports]
from langgraph.checkpoint.mongodb import MongoDBSaver # type: ignore[reportMissingImports]
import os

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# creating a node
def chatbot(state: State):
    messages = [
        {
            "role": "assistant" if isinstance(message, AIMessage) else "user",
            "content": message.content,
        }
        for message in state.get("messages", [])
    ]
    response = client.chat.completions.create(
        model=os.getenv("GOOGLE_MODEL", "gemini-2.0-flash"),
        messages=messages,
    )
    return {"messages": [AIMessage(content=response.choices[0].message.content or "")]}


def sample_node(state: State):
    return {"messages": [AIMessage(content="This is a sample node.")]}


graph_builder = StateGraph(State)

# adding nodes to the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample_node", sample_node)

# adding edges between nodes
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)

# running the graph
graph = graph_builder.compile()

def compile_graph_with_checkpoint(graph):
    DB_URL = "mongodb://root:root@localhost:27017"  # Replace with your MongoDB connection string
    with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:
        graph = graph_builder.compile(checkpointer=checkpointer)
    return graph

graph_with_checkpoint = compile_graph_with_checkpoint(graph)

config = {
    "configurable": {
        "thread_id": "thread_1"
    }
}

result = graph_with_checkpoint.invoke(
State({"messages": [HumanMessage(content="What is the capital of France?")]}), config=config
)
print(result)  # Output: {'messages': ['This is a sample node.']}