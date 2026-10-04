"""planner_node 的测试。"""

import json

from nodes import planner as planner_module
from nodes.planner import planner_node


def test_planner_parses_json_array(monkeypatch):
    monkeypatch.setattr(
        planner_module,
        "call_llm",
        lambda prompt, system="": json.dumps(["市场有多大?", "谁是竞品?"]),
    )

    result = planner_node({"product": "coffee", "region": "China"})

    assert result == {"questions": ["市场有多大?", "谁是竞品?"]}


def test_planner_prompt_contains_product_and_region(monkeypatch):
    captured = {}

    def fake_call_llm(prompt, system=""):
        captured["prompt"] = prompt
        captured["system"] = system
        return "[]"

    monkeypatch.setattr(planner_module, "call_llm", fake_call_llm)

    planner_node({"product": "coffee", "region": "China"})

    assert "coffee" in captured["prompt"]
    assert "China" in captured["prompt"]
    assert captured["system"] == "You are a market research planner."


def test_planner_handles_non_json_response(monkeypatch):
    monkeypatch.setattr(planner_module, "call_llm", lambda prompt, system="": "MOCK_LLM_RESPONSE")

    result = planner_node({"product": "coffee", "region": "China"})

    assert result == {"questions": [], "errors": ["planner: failed to parse LLM response"]}


def test_planner_rejects_non_list_json(monkeypatch):
    monkeypatch.setattr(planner_module, "call_llm", lambda prompt, system="": '{"questions": []}')

    result = planner_node({"product": "coffee", "region": "China"})

    assert result == {"questions": [], "errors": ["planner: failed to parse LLM response"]}


def test_planner_under_mock_llm_env(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")

    result = planner_node({"product": "x", "region": "y"})

    assert "questions" in result or "errors" in result
