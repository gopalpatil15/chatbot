from model_loader import load_model
from chat_memory import ChatMemory

def main():
    print("Chatbot Ready! Type '/exit' to quit.\n")

    qa_bot = load_model()
    memory = ChatMemory(max_turns=3)

    # Load GK facts
    with open("facts.txt", "r") as f:
        base_context = f.read()

    while True:
        user_input = input("User: ")
        if user_input.lower().strip() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        memory.add("User", user_input)

        # Merge facts with short-term memory
        full_context = base_context + "\n" + memory.get_context()
        response = qa_bot(question=user_input, context=full_context)

        if response["score"] < 0.1:
            print("Bot: Sorry, I don't know that one yet.")
        else:
            answer = response["answer"]
            print("Bot:", answer)
            memory.add("Bot", answer)

if __name__ == "__main__":
    main()