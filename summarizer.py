import ollama

def summarize_news(text):
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this news in 3 bullet points:\n{text}"
                }
            ]
        )

        return response['message']['content']

    except Exception as e:
        return f"Error summarizing news: {e}"