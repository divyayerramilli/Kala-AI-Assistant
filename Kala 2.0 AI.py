import openai


openai.api_key = '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'


greeting = "ChatBot: Hi, I'm your new friend, Kala. How can I help you today?"

def chatbot_response(user_input):
   
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100,
        temperature=0.2,  
    )

    return response.choices[0].text.strip()

def complex_chatbot():
    print(greeting)
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    complex_chatbot()
