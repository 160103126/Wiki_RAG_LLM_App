import wikipediaapi
import wikipedia
import requests
from spellchecker import SpellChecker
import re
import spacy


def clean_query(query):
    # Remove special characters and normalize whitespace
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", query)
    cleaned = " ".join(cleaned.split()).lower()
    return cleaned


nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Removes stop words and applies lemmatization."""
    doc = nlp(text)
    
    clean_tokens = [
        token.lemma_ for token in doc 
        if not token.is_stop and not token.is_punct
    ]
    
    return " ".join(clean_tokens)


def get_search_suggestions(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "search": query,
        "limit": 5,
        "namespace": 0,
        "format": "json"
    }
    response = requests.get(url, params=params).json()
    return response[1][0]  # Returns list of suggested titles

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
    user_query = "Who is robert downey"
    # cleaned = clean_query(user_query)  
    cleaned_text = preprocess_text(user_query)
    print('cleaned text:',cleaned_text)
    suggested = get_search_suggestions(cleaned_text)
    print('suggested:',suggested)
    print(search_wikipedia(suggested))
