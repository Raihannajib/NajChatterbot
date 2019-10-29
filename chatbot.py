from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

amitbot = ChatBot('serra')  #changing in variable or name of bot whiile true to false
trained =ListTrainer(amitbot)

for files in os.listdir('english/'):
    data = open('english/'+files,'r').readline()
    trained.train(data)

while False:
    message = input('sir:')
    if message.strip() != 'Bye':
        reply=amitbot.get_response(message)
        print('ChatBot :',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break