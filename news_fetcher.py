import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(topic):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data.get("status") != "ok":
        print("Error from API:", data)
        return []

    articles = data.get("articles", [])

    news_list = []

    for article in articles:
        news_list.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "content": article.get("content"),
            "url": article.get("url")
        })

    return news_list