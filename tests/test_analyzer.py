"""analyzer_node 的测试。"""

from nodes import analyzer as analyzer_module
from nodes.analyzer import analyzer_node


def test_analyzer_returns_analysis(monkeypatch):
    monkeypatch.setattr(
        analyzer_module, "call_llm", lambda prompt, system="": "ANALYSIS"
    )

    result = analyzer_node({"search_results": [{"title": "t", "url": "u", "content": "c"}]})

    assert result == {"analysis": "ANALYSIS"}


def test_analyzer_prompt_contains_results(monkeypatch):
    calls = []

    def fake_call_llm(prompt, system=""):
        calls.append((prompt, system))
        return "ok"

    monkeypatch.setattr(analyzer_module, "call_llm", fake_call_llm)

    analyzer_node(
        {
            "search_results": [
                {"title": "标题A", "url": "http://a", "content": "内容A"},
                {"title": "标题B", "url": "http://b", "content": "内容B"},
            ]
        }
    )

    prompt, system = calls[0]
    assert system == "You are a market research analyst."
    for text in ("标题A", "http://a", "内容A", "标题B", "http://b", "内容B"):
        assert text in prompt


def test_analyzer_missing_search_results(monkeypatch):
    monkeypatch.setattr(
        analyzer_module, "call_llm", lambda prompt, system="": "ANALYSIS"
    )

    result = analyzer_node({})

    assert result == {"analysis": "ANALYSIS"}


def test_analyzer_with_mock_llm_env(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")

    result = analyzer_node({"search_results": [{"title": "t", "url": "u", "content": "c"}]})

    assert result["analysis"] == "MOCK_LLM_RESPONSE"
