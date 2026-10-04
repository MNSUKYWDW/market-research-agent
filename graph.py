"""构建并运行市场调研 Agent 的 LangGraph 图。"""

from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from nodes.analyzer import analyzer_node
from nodes.planner import planner_node
from nodes.retriever import retriever_node
from nodes.writer import writer_node
from state import AgentState


def build_graph() -> CompiledStateGraph:
    """创建并编译市场调研工作流图。"""
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("retriever", retriever_node)
    graph.add_node("analyzer", analyzer_node)
    graph.add_node("writer", writer_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "retriever")
    graph.add_edge("retriever", "analyzer")
    graph.add_edge("analyzer", "writer")
    graph.add_edge("writer", END)

    return graph.compile()


def run(product: str, region: str) -> AgentState:
    """运行完整流程，返回最终状态。"""
    return build_graph().invoke(
        {
            "product": product,
            "region": region,
            "questions": [],
            "search_results": [],
            "analysis": "",
            "report": "",
            "errors": [],
        }
    )
