from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL = "deepseek-r1:8b"


def simple_chat_will_llm_loop() -> None:
    """Run a REPL that sends user input to the LLM and prints responses.

    The loop exits when the user types `/bye`. Handles Ctrl-C and Ctrl-D
    gracefully.

    REPL (Read-Eval-Print Loop) is an interactive programming environment,
    like a command-line console, that lets developers type code, have it
    instantly executed (evaluated) and see the results, then loops back for more input

    """
    print("Hello from langchain_ollama! Type /bye to exit.")

    # Initialize LLM once before the loop
    llm = ChatOllama(model=MODEL, base_url=OLLAMA_BASE_URL)

    try:
        while True:
            try:
                user_input = input(">>> ").strip()
            except EOFError:
                # Ctrl-D / EOF
                print("\nGoodbye!")
                break

            if user_input == "":
                continue

            if user_input == "/bye":
                print("Goodbye!")
                break

            # Send the input to the LLM and print the response.
            try:
                response = llm.invoke(user_input)
            except Exception as e:
                print("Error invoking LLM:", e)
                continue

            print("LLM:", response)

    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")


if __name__ == "__main__":
    simple_chat_will_llm_loop()
