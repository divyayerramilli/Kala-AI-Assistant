import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import openai


openai.api_key = "Ysk-KDDssijKNiMfmKR5OdLQT3BlbkFJyqIXrshRNzo6lbF7KKRZ"

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "All good, thank you!", "I'm fine!"],
    "what is your name": ["I am a chatbot, but you can call me Kala.", "You can call me Kala.", "My name is Kala, I am your new friend."],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how is the weather": ["The weather is sunny today!", "It's raining outside.", "The weather is quite pleasant."],
     "tell me a secret": ["Well, as a chatbot, I have to keep secrets. But here's a fun fact: Bananas are berries, while strawberries are not!"],
    "what's your favorite color?": ["As a chatbot, I don't have preferences, but I think all colors are beautiful!"],
    "can you sing?": ["I'm afraid I don't have a voice, but I can give you the lyrics to your favorite song!"],
    "do you dream": ["In a way, I process information and learn, but I don't experience dreams like humans do."],
    "where do you live": ["I live in the digital world, running on servers and computers."],
    "who is your best friend": ["You are! I'm here to be your friendly chat companion."],
    "tell me a weird fact": ["Bananas are technically berries, but strawberries are not!"],
    "are you human?": ["No, I'm an artificial intelligence programmed to chat with you!"],
    "what's the meaning of life": ["That's a deep question! The meaning of life can vary for each person."],
    "what's the weather in Mars": ["Mars is extremely cold, with temperatures dropping to minus 80 degrees Fahrenheit!"],
     "what is the meaning of life": ["The meaning of life is subjective and can vary from person to person.", "That's a deep question! The meaning of life is a lifelong pursuit of discovering purpose and fulfillment."],
    "why do birds fly?": ["Birds fly as a means of transportation and to find food and shelter.", "Birds have wings that enable them to fly, allowing them to explore their environment and escape predators."],
    "how much wood could a woodchuck chuck if a woodchuck could chuck wood?": ["A woodchuck could chuck as much wood as a woodchuck could chuck if a woodchuck could chuck wood.", "The amount of wood a woodchuck could chuck depends on various factors such as its size, strength, and motivation!"],
    "what is the sound of one hand clapping": ["The sound of one hand clapping is an abstract concept often used in philosophical discussions.", "It's a Zen Buddhist koan meant to provoke thought and challenge conventional thinking."],
    "what came first, the chicken or the egg": ["The question of which came first, the chicken or the egg, is a classic philosophical puzzle.", "It's a paradox that has been debated for centuries, and there is no definitive answer."],
    "can you prove that you are not a robot": ["As an AI-powered chatbot, I am programmed to simulate human-like responses, but I am not a physical entity.", "While I'm not a human, I am designed to provide assistance and engage in conversations like a human would."],
    "tell me a secret": ["I'm an AI chatbot, so I don't have secrets. But here's a fun fact: Penguins have a gland above their eyes that converts seawater into freshwater!", "I'm afraid I can't tell you any secrets, but I can share interesting facts. Did you know that the average person spends six months of their lifetime waiting for red traffic lights to turn green?"],

    "bye": ["Goodbye!", "See you later!", "Bye!"],
     "how's your day": ["It's going great so far!", "It's been a good day, thanks for asking!"],
    "how old are you": ["As an AI, I don't have an age!", "I'm ageless, just like the internet!"],
    "where are you from": ["I exist in the digital world, so I don't have a physical location!", "I'm from the realm of computer programs!"],
    "help": ["How can I help you?", "What can I do for you?"],
    "who created you": ["I was created by Divya Yerramilli."],
    "tell me something": ["Australia is wider than the moon", "Avocados are not vegetables"],
    "what can you do": ["I am a simple conversational friend to provide company and fun facts!"],
    "i have a question": ["I may or may not have the answer. You might have better luck trying a more sophisticated AI."],
    "tell me a joke": ["Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them."],
    "tell me about yourself": ["My name is Kala. I am a friendly AI that can help provide company to you and be a good friend. I love to read and understand the way I work."],
    "i love you": ["Thank you friend! Love is a strong feeling of admiration which I reciprocate!"],
     "what is the time": ["I'm a chatbot, and I don't have access to real-time information."],
    "do you like Python": ["As a chatbot, I don't have feelings, but I think Python is a great programming language!"],
    "thank you": ["You're welcome!", "No problem! It's my pleasure to help.", "You're welcome. If you have any more questions, feel free to ask!"],
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    try:
        response = openai.Completion.create(
            engine="davinci",  
            prompt=user_input,
            max_tokens=5  
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print("Error:", e)
        return "I'm sorry, I don't understand. Can you please say that again?"

def send_message():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    if user_input.lower() == "quit":
        root.quit()
        return
    response = chatbot_response(user_input)
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    chat_window.insert(tk.END, f"Kala: {response}\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def close_chat():
    if messagebox.askokcancel("Kala, AI", "Are you sure you want to quit?"):
        root.quit()

root = tk.Tk()
root.title("ChatBot - Kala")



bg_color = "gold"
chat_bg_color = "black"
user_font = ("Times", 20, "bold")
bot_font = ("Merriweather", 20)
user_color = "red"
bot_color = "black"

chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True)


chat_window = tk.Text(root, bg="lightgrey", wrap=tk.WORD,font=bot_font,)
chat_window.tag_configure("user", foreground="black",font=bot_font,)
chat_window.tag_configure("bot", foreground="darkslategrey",font=bot_font)
chat_window.pack(padx=25, pady=25, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.DISABLED)


scrollbar = tk.Scrollbar(chat_frame, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_window.config(yscrollcommand=scrollbar.set)



user_entry = tk.Entry(root, bg="cadetblue",font=bot_font, fg=bot_color)
user_entry.pack(padx=10, pady=15, fill=tk.BOTH)


send_button = tk.Button(root, text="SEND", font=("Verdana", 25, "bold"), fg="teal", bg="lightcoral", command=send_message)
send_button.pack(padx=10, pady=5, fill=tk.BOTH)

root.bind("<Return>", lambda event: send_message())
n
root.protocol("WM_DELETE_WINDOW", close_chat)

root.mainloop()

