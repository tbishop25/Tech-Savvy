from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import time
time.clock = time.time

app = Flask(__name__)


chatbot = ChatBot("TS")
trainer = ListTrainer(chatbot)

trainer.train([
    'Hi',
    'Hello',
    'I need help',
    'What do you need assistance with?',
    'I need help with Word',
    'Okay choose an option'
])
trainer.train([
    "I need help?",
    "What do you need help with?",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
