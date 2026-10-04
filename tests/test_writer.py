"""writer_node 的测试。"""

from nodes import writer as writer_module
from nodes.writer import writer_node


def test_writer_returns_report(monkeypatch):
    monkeypatch.setattr(
        writer_module, "call_llm", lambda prompt, system="": "REPORT"
    )

    result = writer_node({"product": "x", "region": "y", "analysis": "a"})

    assert result == {"report": "REPORT"}


def test_writer_prompt_contains_state(monkeypatch):
    calls = []

    def fake_call_llm(prompt, system=""):
        calls.append((prompt, system))
        return "ok"

    monkeypatch.setattr(writer_module, "call_llm", fake_call_llm)

    writer_node({"product": "智能手机", "region": "东南亚", "analysis": "分析内容"})

    prompt, system = calls[0]
    assert system == "You are a report writer."
    for text in ("智能手机", "东南亚", "分析内容"):
        assert text in prompt


def test_writer_missing_fields(monkeypatch):
    monkeypatch.setattr(
        writer_module, "call_llm", lambda prompt, system="": "REPORT"
    )

    result = writer_node({})

    assert result == {"report": "REPORT"}


def test_writer_with_mock_llm_env(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")

    result = writer_node({"product": "x", "region": "y", "analysis": "a"})

    assert result["report"] == "MOCK_LLM_RESPONSE"
