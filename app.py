import streamlit as st
from news_fetcher import fetch_news
from rag_pipeline import NewsRAG

# Initialize RAG system
rag = NewsRAG()

st.set_page_config(page_title="AI News Research Agent", layout="wide")

st.title("🧠 AI News Research Agent")
st.write("Search for the latest news and ask questions about them.")

# Topic input
topic = st.text_input("Enter a topic (AI, startups, business, etc.)")

# Fetch news button
if st.button("Fetch News"):

    if topic:

        articles = fetch_news(topic)

        if len(articles) == 0:
            st.error("No news found for this topic.")
        else:

            rag.add_news(articles)

            st.success(f"{len(articles)} articles added to the knowledge base.")

            st.subheader("Latest News")

            for article in articles:

                st.markdown(f"### {article['title']}")

                if article.get("description"):
                    st.write(article["description"])

                if article.get("url"):
                    st.markdown(f"[Read full article]({article['url']})")

                st.divider()


# Ask question section
st.subheader("Ask Questions About the News")

question = st.text_input("Example: What are the latest AI trends?")

if st.button("Ask AI"):

    if question:
        answer = rag.ask(question)

        st.subheader("AI Answer")
        st.write(answer)