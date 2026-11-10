from dotenv import load_dotenv # type: ignore[reportMissingImports]
load_dotenv()  # Load environment variables from .

from typing_extensions import TypedDict # type: ignore[reportMissingImports]
from typing import Literal, Optional
from langgraph.graph import START, END, StateGraph # type: ignore[reportMissingImports]
from openai import OpenAI # type: ignore[reportMissingImports]
import os

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class state(TypedDict):
    user_input: str
    llm_response: Optional[str]

    is_good: Optional[bool]

def chatbot(state:state):
    response = client.chat.completions.create(
        model="gemini-pro",
        messages=[
            {"role": "user", "content": state.get("user_input", "")}
        ]
    )

    state["llm_response"] = response.choices[0].message.content
    return state

def evaluate_response(state:state) -> Literal["endNode", "chatboat_otherAi"]:
    if True: 
        return "endNode"
    else:
     return "chatboat_otherAi"

def chatboat_otherAi(state:state):
    response = client.chat.completions.create(
        model="gemini-pro",
        messages=[
            {"role": "user", "content": state.get("llm_response", "")}
        ]
    )

    state["llm_response"] = response.choices[0].message.content
    return state

def endNode(state:state):
    print("Final LLM Response:", state.get("llm_response", ""))
    return state

graph_builder = StateGraph(state)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("evaluate_response", evaluate_response)
graph_builder.add_node("chatboat_otherAi", chatboat_otherAi)
graph_builder.add_node("endNode", endNode)

graph_builder.add_edge(START, "evaluate_response")
graph_builder.add_conditional_edges("chatbot", "evaluate_response")

graph_builder.add_edge("endNode", END)


graph = graph_builder.compile()
graph.invoke(state({"user_input": "What is the capital of France?"}))