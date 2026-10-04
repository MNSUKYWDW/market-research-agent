"""端到端测试：在 mock 环境（MOCK_LLM=1 / MOCK_SEARCH=1）下运行完整图。"""

import pytest

import graph


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")
    monkeypatch.setenv("MOCK_SEARCH", "1")


@pytest.fixture
def state(mock_env):
    return graph.run("Notion", "Southeast Asia")


def test_run_keeps_input_fields(state):
    assert state["product"] == "Notion"
    assert state["region"] == "Southeast Asia"


def test_run_produces_report(state):
    assert isinstance(state["report"], str)
    assert state["report"]


def test_run_fills_intermediate_fields(state):
    assert isinstance(state["questions"], list)
    assert isinstance(state["search_results"], list)
    assert isinstance(state["analysis"], str)
