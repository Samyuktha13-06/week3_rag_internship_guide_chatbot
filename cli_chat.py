from rag.rag_chain import ask_question


def main():

    print("=" * 70)
    print("🤖 DStarix Internship Guide Chatbot")
    print("=" * 70)
    print("Ask questions about the internship.")
    print("Type 'exit' or 'quit' to end the chat.")

    while True:

        question = input("\nYou: ").strip()

        if not question:
            print("Bot: Please enter a question.")
            continue

        if question.lower() in ["exit", "quit"]:
            print("\nBot: Thank you! Good luck with your internship. 👋")
            break

        try:

            response = ask_question(question)

            print(f"\nBot: {response}")

        except Exception as e:

            print(f"\nError: {e}")


if __name__ == "__main__":
    main()