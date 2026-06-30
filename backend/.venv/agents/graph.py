from typing import TypedDict

from langgraph.graph import START, END, StateGraph

from agents.planner import detect_intent
from agents.tools import (
    qa_tool,
    summary_tool,
    compare_tool,
)


class GraphState(TypedDict):

    question: str

    intent: str

    answer: str



# Nodes


def planner_node(state: GraphState):

    intent = detect_intent(state["question"])

    return {
        "intent": intent
    }


def qa_node(state: GraphState):

    result = qa_tool(state["question"])

    return {
        "answer": result["answer"]
    }


def summary_node(state: GraphState):

    result = summary_tool(state["question"])

    return {
        "answer": result["answer"]
    }


def compare_node(state: GraphState):

    result = compare_tool(state["question"])

    return {
        "answer": result["answer"]
    }



# Router


def route(state: GraphState):

    intent = state["intent"]

    if intent == "SUMMARY":
        return "summary"

    if intent == "COMPARE":
        return "compare"

    return "qa"



# Graph


builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)
builder.add_node("qa", qa_node)
builder.add_node("summary", summary_node)
builder.add_node("compare", compare_node)

builder.add_edge(START, "planner")

builder.add_conditional_edges(
    "planner",
    route,
    {
        "qa": "qa",
        "summary": "summary",
        "compare": "compare",
    },
)

builder.add_edge("qa", END)
builder.add_edge("summary", END)
builder.add_edge("compare", END)

graph = builder.compile()