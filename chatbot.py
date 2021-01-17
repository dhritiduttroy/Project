from chatterbot.trainers import ListTrainer
from chatbot import Chatbot

bot= Chatbot{'Text'}
copy = open {'chatbot.txt','r'}.readlines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request = input('you')
    response= bot.get_response(request)
    print('Bot ', response)