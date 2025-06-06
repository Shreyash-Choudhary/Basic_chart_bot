import time

# 🛒 Grocery Store Chatbot with enhanced features

def slow_print(text):
    """Simulate typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def grocery_bot():
    slow_print("🛒 Hello! Welcome to FreshMart Grocery Store.")
    name = input("May I know your name? \nYou: ").strip().title()
    slow_print(f"Hi {name}! How can I assist you today? (Type 'help' to see common questions)")

    # Define keyword-based FAQs (more flexible than exact phrases)
    faqs = {
        "opening hours": "We are open from 8 AM to 9 PM, every day including weekends.",
        "location": "We are located at 456 Market Lane, GreenTown.",
        "delivery": "Yes, we offer free home delivery for orders above ₹500.",
        "products": "We sell fresh vegetables, fruits, dairy, snacks, grains, and household items.",
        "contact": "You can call us at 98765-43210 or email support@freshmart.in"
    }

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    while True:
        user_input = input("\nYou: ").strip().lower()

        # Exit conditions
        if user_input in ["exit", "quit", "bye"]:
            slow_print(f"Bot: Thank you for visiting FreshMart, {name}. Have a fresh and healthy day! 🌽")
            break

        # Greeting response
        elif user_input in greetings:
            slow_print("Bot: Hello! How can I help you today?")

        # Help command
        elif user_input == "help":
            slow_print("Bot: You can ask things like:")
            for question in faqs:
                slow_print(f"- {question.capitalize()}?")

        # FAQ keyword detection
        else:
            found = False
            for keyword in faqs:
                if keyword in user_input:
                    slow_print(f"Bot: {faqs[keyword]}")
                    found = True
                    break
            if not found:
                slow_print("Bot: Sorry, I don’t know that yet. 🫤 (Type 'help' to see what I can answer.)")

# Run the bot
if __name__ == "__main__":
    grocery_bot()
