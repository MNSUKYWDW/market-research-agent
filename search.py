import os


def search(query: str, max_results: int = 3) -> list[dict]:
    if os.environ.get("MOCK_SEARCH") == "1":
        return [
            {
                "title": "Mock Result",
                "url": "https://example.com",
                "content": "mock content",
            }
        ]

    from tavily import TavilyClient

    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = client.search(query, max_results=max_results)
    return [
        {"title": r["title"], "url": r["url"], "content": r["content"]}
        for r in response["results"]
    ]
