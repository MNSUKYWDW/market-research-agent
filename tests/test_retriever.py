"""retriever_node 的测试。"""

from nodes import retriever as retriever_module
from nodes.retriever import retriever_node


def test_retriever_merges_results(monkeypatch):
    monkeypatch.setattr(
        retriever_module,
        "search",
        lambda query, max_results=3: [{"title": query, "url": "u", "content": "c"}],
    )

    result = retriever_node({"questions": ["q1", "q2"]})

    assert result == {
        "search_results": [
            {"title": "q1", "url": "u", "content": "c"},
            {"title": "q2", "url": "u", "content": "c"},
        ]
    }


def test_retriever_empty_questions(monkeypatch):
    calls = []
    monkeypatch.setattr(
        retriever_module, "search", lambda query, max_results=3: calls.append(query) or []
    )

    result = retriever_node({"questions": []})

    assert result == {"search_results": []}
    assert calls == []


def test_retriever_with_mock_search_env(monkeypatch):
    monkeypatch.setenv("MOCK_SEARCH", "1")

    result = retriever_node({"questions": ["q1", "q2"]})

    assert len(result["search_results"]) == 2
