import wikipediaapi
import wikipedia
import requests

def search_wikipedia(query: str, lang: str = "en", max_results: int = 3):
    """Search Wikipedia and return multiple relevant page summaries."""
    user_agent = "WikiRAGApp/1.0 (pradeeplachireddy@gmail.com)"  # Set a valid User-Agent
    wiki_wiki = wikipediaapi.Wikipedia(language=lang, user_agent=user_agent)

    # Wikipedia search API
    search_url = f"https://{lang}.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": max_results,
    }
    response = requests.get(search_url, params=search_params, headers={"User-Agent": user_agent})
    search_results = response.json().get("query", {}).get("search", [])

    if not search_results:
        return {"error": "No relevant pages found."}

    # Get full content using page IDs instead of titles
    page_ids = [str(item["pageid"]) for item in search_results]
    page_url = f"https://{lang}.wikipedia.org/w/api.php"
    page_params = {
        "action": "query",
        "format": "json",
        "pageids": "|".join(page_ids),  # Fetch multiple pages
        "prop": "extracts",
        "explaintext": True,  # Get plain text content
        "exlimit": max_results
    }
    page_response = requests.get(page_url, params=page_params, headers={"User-Agent": user_agent})
    pages_data = page_response.json().get("query", {}).get("pages", {})

    results = {page["title"]: page.get("extract", "No content available") for page in pages_data.values()}

    return results

if __name__=="__main__":
    print(search_wikipedia('Neural Networks'))
