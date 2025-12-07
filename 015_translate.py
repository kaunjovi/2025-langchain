from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL = "deepseek-r1:8b"


def translate(message: str = "Hello world", language: str = "Hindi") -> None:
    llm = ChatOllama(model=MODEL, base_url=OLLAMA_BASE_URL)

    messages = [
        (
            "system",
            "You are a helpful translator. Translate the user sentence in the language requested.",
        ),
        ("human", f"Translate {message} in {language} language."),
    ]

    response = llm.invoke(messages)
    print(f"LLM Response:{response.text}")


if __name__ == "__main__":
    translate("How are you doing?", "Hindi")
