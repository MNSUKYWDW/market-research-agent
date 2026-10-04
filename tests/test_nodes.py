"""各节点在 mock 环境（MOCK_LLM=1 / MOCK_SEARCH=1）下的集成测试。"""

import pytest

from nodes.analyzer import analyzer_node
from nodes.planner import planner_node
from nodes.retriever import retriever_node
from nodes.writer import writer_node


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "1")
    monkeypatch.setenv("MOCK_SEARCH", "1")


def test_planner_node():
    result = planner_node({"product": "x", "region": "y"})

    assert isinstance(result, dict)
    assert "questions" in result or "errors" in result


def test_retriever_node():
    result = retriever_node({"questions": ["q1"]})

    assert isinstance(result, dict)
    assert "search_results" in result
    assert len(result["search_results"]) > 0


def test_analyzer_node():
    result = analyzer_node(
        {"search_results": [{"title": "t", "url": "u", "content": "c"}]}
    )

    assert isinstance(result, dict)
    assert "analysis" in result


def test_writer_node():
    result = writer_node({"product": "x", "region": "y", "analysis": "a"})

    assert isinstance(result, dict)
    assert "report" in result
