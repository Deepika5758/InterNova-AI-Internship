
# InterNova Internship - Week 1
# Project: Rule-Based AI Chatbot

print("=" * 45)
print("       WELCOME TO AI CHATBOT")
print("=" * 45)

print("Bot: Hello! I am your AI chatbot.")
print("Bot: You can ask me basic questions.")
print("Bot: Type 'bye' to end the conversation.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Welcome. How can I help you?")

    elif user_input in ["how are you","How are you","How are you?", "how are you?"]:
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input in ["what is your name", "what is your name?"]:
        print("Bot: I am InterNova AI Chatbot.")

    elif user_input in ["what is ai", "what is ai?"]:
        print("Bot: Artificial Intelligence enables machines")
        print("to perform tasks that require human intelligence.")

    elif user_input in ["what is python", "what is python?"]:
        print("Bot: Python is a popular programming language")
        print("widely used in AI, ML and data science.")

    elif user_input in ["what can you do", "help"]:
        print("Bot: I can answer basic questions about AI and Python.")

    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome! Happy to help.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Please try asking something else.")

print("\nChatbot session ended.")
