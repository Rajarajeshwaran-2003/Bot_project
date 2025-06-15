# This is just for generating the response list (not used in the Django app directly)
from bot import base_responses, qa_responses, random_responses
import random

responses = []

for keyword in base_responses:
    responses.extend(base_responses[keyword])
for keyword in qa_responses:
    responses.extend(qa_responses[keyword])
while len(responses) < 1000:
    responses.append(random.choice(random_responses))

random.shuffle(responses)

with open("bot_responses.txt", "w") as f:
    for r in responses:
        f.write(r + "\n")

print("Saved 1000 chatbot responses.")
