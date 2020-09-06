from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json
import pyttsx3
import datetime
import random

ChatBot = ChatBot(name = 'BankBot',
                  read_only = False,
                  logic_adapters = ["chatterbot.logic.BestMatch"],
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")
corpus_trainer = ChatterBotCorpusTrainer(ChatBot)
corpus_trainer.train("chatterbot.corpus.english")
greet_conversation = [
    "yes",
    "ok",
    "good",
    "glad to hear it"
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "how are you?",
    "i am ok",
    "are you ok?",
    random.choice(["yes Why not?", 'It dependes']),
    "How old are you",
    "I burned In 2020 09/01/20",
    "what is linux",
    "it is a kernel created by linus trovalds",
    "what is kernel?",
    "it is computer core",
]

questions = [
'what time is it?',
datetime.datetime.now().strftime("%D %H %M")
]

persian = [
"do you know persian?",
"yes",
"can you talk persian?",
"yes",
"talk persian please",
random.choice(['سلام', 'خوبی', 'چه خبر']),
"سلام",
"سلام دوست عزیز",
"خوبی",
"ممنون بله خوبم",
"چطوری",
"خوبم",
"چه خبر",
"سلامتی",
"حالت خوبه؟",
"بله چرا که نه"
]

personal_info = [
"when is your birthday?",
'2020 09/01/20',
'what is your name?',
'adam',


]
#Initializing Trainer Object
trainer = ListTrainer(ChatBot)

#Training BankBot
trainer.train(greet_conversation)
#trainer.train(open_timings_conversation)
#trainer.train(close_timings_conversation)
trainer.train(personal_info)
trainer.train(persian)
trainer.train(questions)


s = pyttsx3.init()
s.setProperty('rate', '110')
while (True):
    user_input = input("You:")
    if (user_input == 'quit'):
        break
    response = ChatBot.get_response(user_input)
    print(f'ai : {response}')
    s.say(response)
    s.runAndWait()
