from typing_extensions import TypedDict # type: ignore[reportMissingImports]
from typing import Annotated
from langgaph.graph.message import add_messages # type: ignore[reportMissingImports]
from langgaph.graph import StateGraph # type: ignore[reportMissingImports]

class state(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(state)