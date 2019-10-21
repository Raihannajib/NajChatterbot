from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

surajbot = ChatBot('gaurav')
trainer =ListTrainer(surajbot)               #changing the name of the bot to surajbot and name of the bot to gaurav

for files in os.listdir('english/'):
    data = open('english/'+files,'r').readline()
    trainer.train(data)

while True:
    message = input('sir:')
    if message.strip() != 'Bye':
        response1=nsurajbot.get_response(message)
        print('ChatBot :',response1)                                      #changing the name of variable to response 1
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break
