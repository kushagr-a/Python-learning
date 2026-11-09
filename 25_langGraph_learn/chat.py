from dotenv import load_dotenv # type: ignore[reportMissingImports]
load_dotenv()  # Load environment variables from .

from sre_parse import State

from typing_extensions import TypedDict # type: ignore[reportMissingImports]
from typing import Annotated
from langgaph.graph.message import add_messages # type: ignore[reportMissingImports]
from langgaph.graph import StateGraph, START, END # type: ignore[reportMissingImports]
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gemini-pro",
    provider="google",
)
class state(TypedDict):
    messages: Annotated[list, add_messages]

# creating a node
def chatbot(state:state):
    response = llm.invoke(state.get("messages", []))
    return {"messages": [response]}

def sampleNode(state:state):
    return {"messages": ["This is a sample node."]}

graph_builder = StateGraph(state)

# adding nodes to the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sampleNode", sampleNode)

# adding edges between nodes
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sampleNode")
graph_builder.add_edge("sampleNode", END)

# running the graph
graph = graph_builder.compile()

result = graph.invoke(State({"messages": ["What is the capital of France?"]}))
print(result)  # Output: {'messages': ['This is a sample node.']}