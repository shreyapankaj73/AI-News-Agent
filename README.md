# 🧠 AI News Research Agent

An AI-powered app that:
- Fetches latest news using APIs
- Uses RAG (Retrieval-Augmented Generation)
- Answers questions based on real-time news

---

## 🚀 Features
- 🔍 Topic-based news search
- 🧠 AI-generated answers
- ⚡ Fast retrieval using vector database

---

## 🛠 Tech Stack
- Streamlit (Frontend)
- LangChain (RAG pipeline)
- ChromaDB (Vector database)
- HuggingFace Embeddings

---

## ▶️ How to Run

1. Clone the repository
git clone https://github.com/shreyapankaj73/AI-News-Agent.git

2. Navigate to the folder
cd AI-News-Agent

3. Install dependencies
pip install -r requirements.txt

4. Add your API key in a .env file
NEWS_API_KEY=your_newsapi_key_here

5. Run the app
python -m streamlit run app.py