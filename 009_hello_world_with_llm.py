from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL = "deepseek-r1:8b"


def hello_world_with_llm() -> None:
    llm = ChatOllama(model=MODEL, base_url=OLLAMA_BASE_URL)
    response = llm.invoke("Hello, world, from LangChain Ollama!")
    print(f"LLM Response:{response.text}")


if __name__ == "__main__":
    hello_world_with_llm()
