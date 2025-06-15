import random
from fuzzywuzzy import process

# Define core response sets
base_responses = {
    "hello": [
        "Hi there! How can I help you?",
        "Hello! What can I do for you today?",
        "Hey! Nice to see you.",
        "Greetings! How may I assist you?"
    ],
    "bye": [
        "Goodbye! Have a great day.",
        "See you later!",
        "Bye! Come back soon.",
        "Farewell! Take care."
    ],
    "how are you": [
        "I'm just a bot, but I'm doing fine. Thanks for asking!",
        "I'm always ready to help!",
        "Doing great! How about you?",
        "I'm a bot, so I don't have feelings, but I'm functioning well!"
    ]
}

qa_responses = {
    "what's your name": [
        "I'm just a chatbot!", "Call me Bot.", "I don't have a name, but you can call me Helper."
    ],
    "tell me a joke": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "what time is it": [
        "I don’t have a clock, but you can check your device!", "Time for you to get a watch! 😄"
    ],
    "how old are you": [
        "I was just born (digitally speaking)!", "Age is just a number for a bot like me."
    ],
    "who made you": [
        "I was created by a developer using Python!", "A human programmed me to chat with you."
    ],
    "what can you do": [
        "I can answer simple questions, say hello, and goodbye!", "Try asking me how I am or tell me a joke!"
    ]
}

random_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting question! I'm still learning.",
    "Let me think about that...",
    "I don’t have an answer for that yet.",
    "Ask me something else!",
    "I’m just a simple chatbot, but I’ll try my best.",
    "Hmm, I need more information.",
    "Can you ask in a different way?",
    "I’m designed to answer simple questions.",
    "Sorry, I didn’t catch that."
]

# Combine all response keys
all_keys = list(base_responses.keys()) + list(qa_responses.keys())
THRESHOLD = 80  # similarity threshold

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Direct match
    if user_input in base_responses:
        return random.choice(base_responses[user_input])
    elif user_input in qa_responses:
        return random.choice(qa_responses[user_input])

    # Loose keyword match
    for key in base_responses:
        if key in user_input:
            return random.choice(base_responses[key])
    for key in qa_responses:
        if key in user_input:
            return random.choice(qa_responses[key])

    # Fuzzy match if input is close to a known phrase
    match, score = process.extractOne(user_input, all_keys)
    if score >= THRESHOLD:
        if match in base_responses:
            return random.choice(base_responses[match])
        elif match in qa_responses:
            return random.choice(qa_responses[match])

    # Fallback
    return random.choice(random_responses)
