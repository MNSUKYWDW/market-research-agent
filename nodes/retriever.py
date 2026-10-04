"""检索节点：针对每个调研问题搜索并合并结果。"""

from search import search


def retriever_node(state: dict) -> dict:
    questions = state.get("questions", [])

    all_results = []
    for question in questions:
        all_results.extend(search(question))

    return {"search_results": all_results}
