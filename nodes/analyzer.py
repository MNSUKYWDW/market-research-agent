"""分析节点：根据检索结果生成市场分析。"""

from llm import call_llm

SYSTEM = "You are a market research analyst."


def analyzer_node(state: dict) -> dict:
    search_results = state.get("search_results", [])

    formatted = "\n".join(
        f"- {result.get('title', '')} ({result.get('url', '')}): "
        f"{result.get('content', '')}"
        for result in search_results
    )

    prompt = (
        "Analyze the following market research findings and summarize the key "
        "insights about the market:\n\n" + formatted
    )

    response = call_llm(prompt, system=SYSTEM)

    return {"analysis": response}
