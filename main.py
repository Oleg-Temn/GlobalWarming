import telebot
import random
import os

list_of_facts = ["тут", "вы", "можете", "перечислять", "различные факты"]
bot = telebot.TeleBot(token=os.getenv('TG_API_TOKEN'))

@bot.message_handler(commands=["start"])
def start(message):
    text = "[Ваше приветствие]"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def rando(message):
    r = random.randint(0, (list_of_facts.len - 1))
    bot.send_message(message.chat.id, list_of_facts[r])

#Здесь вы можете продолжить писать различные команды