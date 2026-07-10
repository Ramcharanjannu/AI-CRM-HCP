from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.ai.tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    generate_summary,
    recommend_followup
)


class AgentState(TypedDict):
    user_input: str
    tool_name: str
    result: str


def tool_router(state: AgentState):

    tool = state["tool_name"]
    text = state["user_input"]

    if tool == "log":
        output = log_interaction.invoke(text)

    elif tool == "edit":
        output = edit_interaction.invoke(text)

    elif tool == "search":
        output = search_hcp.invoke(text)

    elif tool == "summary":
        output = generate_summary.invoke(text)

    elif tool == "followup":
        output = recommend_followup.invoke(text)

    else:
        output = "Invalid Tool"

    return {"result": output}


builder = StateGraph(AgentState)

builder.add_node("tool_router", tool_router)

builder.add_edge(START, "tool_router")

builder.add_edge("tool_router", END)

graph = builder.compile()