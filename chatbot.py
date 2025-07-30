# Install required packages first:
# pip install chatterbot==1.0.5
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'corona bot',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'  # Ensure a persistent DB
)

# Create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Get a response to an input statement
response = chatbot.get_response('What is your number?')
print(f"Bot: {response}")

response = chatbot.get_response('Who are you?')
print(f"Bot: {response}")
