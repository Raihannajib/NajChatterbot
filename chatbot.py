from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

najibBot = ChatBot('Bot')
trainer =ListTrainer(najibBot)

for files in os.listdir('english/'):
    data = open('english/'+files,'r').readline()
    trainer.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply=najibBot.get_response(message)
        print('ChatBot :',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break