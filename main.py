from news_fetcher import fetch_news
from summarizer import summarize_news
from rag_pipeline import NewsRAG

rag = NewsRAG()

topic = input("Enter topic: ")

articles = fetch_news(topic)

rag.store_articles(articles)

question = input("\nAsk a question about the news: ")

docs = rag.retrieve(question)

context = "\n".join(docs)

answer = summarize_news(f"""
Use the following news articles to answer the question:

{context}

Question: {question}
""")

print("\nAnswer:")
print(answer)