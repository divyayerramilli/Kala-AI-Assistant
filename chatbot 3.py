import random

# Define the Chatbot Responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "All good, thank you!", "I'm fine!"],
    "what is your name": ["I am a chatbot, but you can call me Kala.", "You can call me Kala.", "My name is Kala, I am your new friend."],
    "hello": ["Hello!", "Hi there!", "Hey!"],

    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "help": ["How can I help you?", "What can I do for you?"],
    "tell me something": ["Australia is wider than the moon", "Avocados are not vegetables"],
    "what can you do": ["I am a simple conversational friend to provide company and fun facts!"],
    "i have a question": ["I may or may not have the answer. You might have better luck trying a more sophisticated AI."],
    "tell me a joke": ["Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them."],
    "tell me about yourself": ["My name is Kala. I am a friendly AI that can help provide company to you and be a good friend. I love to read and understand the way I work."],
    "I love you": ["Thank you friend! Love is a strong feeling of admiration which I reciprocate!"]
    
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand. Can you please say that again?"

def simple_chatbot():
    print("ChatBot: Hi, I'm your new friend, Kala. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    simple_chatbot()
