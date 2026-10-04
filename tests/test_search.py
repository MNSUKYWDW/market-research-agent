"""search 的测试（MOCK_SEARCH=1 模式）。"""

from search import search


def test_search_returns_list_of_dicts(monkeypatch):
    monkeypatch.setenv("MOCK_SEARCH", "1")

    results = search("test query")

    assert isinstance(results, list)
    assert len(results) > 0
    for item in results:
        assert isinstance(item, dict)


def test_search_results_have_required_keys(monkeypatch):
    monkeypatch.setenv("MOCK_SEARCH", "1")

    results = search("test query")

    for item in results:
        assert {"title", "url", "content"} <= set(item)


def test_search_result_values_non_empty(monkeypatch):
    monkeypatch.setenv("MOCK_SEARCH", "1")

    results = search("test query")

    for item in results:
        for key in ("title", "url", "content"):
            assert item[key]
