"""写作节点：根据分析结果生成 markdown 市场调研报告。"""

from llm import call_llm

SYSTEM = "You are a report writer."


def writer_node(state: dict) -> dict:
    product = state.get("product", "")
    region = state.get("region", "")
    analysis = state.get("analysis", "")

    prompt = (
        "Write a market research report in Markdown for the product "
        f"{product!r} in the region {region!r}, based on the following "
        "analysis:\n\n" + analysis
    )

    response = call_llm(prompt, system=SYSTEM)

    return {"report": response}
