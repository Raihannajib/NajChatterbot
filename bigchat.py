__author__="najib"


"""from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#create a new chat  bot
Chatnajib = ChatBot("Bot")

#training my chatbot bot starts with knowledge
from chatterbot.trainers import ListTrainer
conversation = ["hello",
                "hi there!",
                "how are you?",
                "great hamdollah",
                "thank u",
                "u'are welcom."]
trainer = ListTrainer(chatnajib)
trainer.train(conversation)

#get a reponse
reponse = chatnajib.get_response("Good morning")
print(reponse)"""

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
response = chatbot.get_response("Good morning!")
print(response)