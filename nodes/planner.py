"""规划节点：根据产品和地区生成市场调研问题列表。"""

import json

from llm import call_llm

SYSTEM = "You are a market research planner."


def planner_node(state: dict) -> dict:
    product = state.get("product", "")
    region = state.get("region", "")

    prompt = (
        f"Create market research questions for the product '{product}' "
        f"in the region '{region}'.\n"
        "Return ONLY a JSON array of question strings, e.g. "
        '["question 1", "question 2"]. No extra text.'
    )

    response = call_llm(prompt, system=SYSTEM)

    try:
        questions = json.loads(response)
    except (TypeError, ValueError):
        return {"questions": [], "errors": ["planner: failed to parse LLM response"]}

    if not isinstance(questions, list):
        return {"questions": [], "errors": ["planner: failed to parse LLM response"]}

    return {"questions": [str(q) for q in questions]}
