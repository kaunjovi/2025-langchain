from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL = "deepseek-r1:8b"


def respond_as_a_stream(city: str = "Delhi") -> None:
    llm = ChatOllama(model=MODEL, base_url=OLLAMA_BASE_URL)

    messages = [
        (
            "system",
            "You are a local guide to India. Help create visitors a detailed itinerary for their trip based on their preferences.",
        ),
        (
            "human",
            f"I am planning a trip to {city}. Can you suggest an itinerary for me please",
        ),
    ]

    # response = llm.invoke(messages)

    for chunk in llm.stream(messages):
        print(chunk.text, end="")

    # print(f"LLM Response:{response.text}")


if __name__ == "__main__":
    respond_as_a_stream()
