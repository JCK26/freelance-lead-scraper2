from duckduckgo_search import DDGS

SEARCH_QUERIES = [
    "hiring virtual assistant",
    "outsourcing admin tasks",
    "looking for administrative support",
    "operations assistant needed",
    "small business admin help"
]

def find_websites():
    urls = set()
    with DDGS() as ddgs:
        for query in SEARCH_QUERIES:
            results = ddgs.text(query, max_results=15)
            for r in results:
                urls.add(r["href"])
    return list(urls)
