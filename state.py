"""市场研究 Agent 的状态定义。"""

from typing import TypedDict


class AgentState(TypedDict):
    """在图节点之间传递的共享状态。"""

    product: str
    region: str
    questions: list[str]
    search_results: list[dict]
    analysis: str
    report: str
    errors: list[str]
