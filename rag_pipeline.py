from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


class NewsRAG:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = Chroma(
            collection_name="news_collection",
            embedding_function=self.embeddings,
            persist_directory="./chroma_db"
        )


    def add_news(self, articles):

        docs = []

        for article in articles:

            content = f"""
            Title: {article.get("title")}
            Description: {article.get("description")}
            Content: {article.get("content")}
            """

            docs.append(Document(page_content=content))

        if docs:
            self.vectorstore.add_documents(docs)


    def ask(self, question):

        results = self.vectorstore.similarity_search(question, k=3)

        if not results:
            return "No relevant news found."

        context = "\n\n".join([doc.page_content for doc in results])

        # Simple AI-style explanation
        answer = f"""
Based on the latest news articles, here are the key insights about your question:

{question}

Key information from recent news:

{context}

Summary:
These articles highlight the latest developments related to your question. 
Major themes include AI tools, enterprise AI platforms, and new AI research developments.
"""

        return answer