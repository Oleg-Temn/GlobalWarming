import telebot
import random
import os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
bot = telebot.TeleBot(token=os.getenv('TG_API_TOKEN'))

#Функции с фактами

def fact1(message):
    text = "Ископаемое топливо (уголь, нефть, газ) обеспечивает более 75% глобальных выбросов парниковых газов, задерживающих тепло."
    bot.send_message(message.chat.id, text)

def fact2(message):
    text = "В России потепление происходит в 2,7 раза быстрее, чем в среднем по земному шару."
    bot.send_message(message.chat.id, text)

def fact3(message):
    text = "Гренландия теряет около 279 миллиардов тонн льда ежегодно."
    bot.send_message(message.chat.id, text)

def fact4(message):
    text = "За XX век уровень мирового океана поднялся на 20 см, и темпы роста ускоряются."
    bot.send_message(message.chat.id, text)

def fact5(message):
    text = "Потепление вызывает засухи, голод и разрушение экосистем."
    bot.send_message(message.chat.id, text)

def fact6(message):
    text = "Период 2010–2019 годов стал самым теплым десятилетием за всю историю наблюдений."
    bot.send_message(message.chat.id, text)

def fact7(message):
    text = "Из-за тепла малярийные комары и клещи захватывают новые территории ООН."
    bot.send_message(message.chat.id, text)

def fact8(message):
    text = "У некоторых рептилий, например зеленых черепах, пол потомства зависит от тепла, из-за чего сейчас рождается до 99% самок."
    bot.send_message(message.chat.id, text)

def fact9(message):
    text = "Таяние полярных льдов перераспределяет массу воды к экватору, что незначительно замедляет вращение планеты и удлиняет сутки."
    bot.send_message(message.chat.id, text)

def fact10(message):
    text = "Из-за рекордного потепления за последние 40 лет площадь растительного покрова (мхов и лишайников) на Антарктическом полуострове увеличилась почти в 14 раз."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["start"])
def start(message):
    text = "Добро пожаловать в лучшего обучающего телеграмм-бота по глобальному потеплению"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random_fact"])
def rando(message):
    function = random.randint(1, 10)
    match function:
        case 1:
            fact1(message)
        case 2:
            fact2(message)
        case 3:
            fact3(message)
        case 4:
            fact4(message)
        case 5:
            fact5(message)
        case 6:
            fact6(message)
        case 7:
            fact7(message)
        case 8:
            fact8(message)
        case 9:
            fact9(message)
        case 10:
            fact10(message)

class Plants:
    def __init__(self, chatid, water, ripeness):
        self.chatid = chatid
        self.water = water
        self.ripeness = ripeness


level = None
dop1 = ""

@bot.message_handler(commands=["start_game"])
def start_game(message):
    # Создаем объект клавиатуры
    markup = InlineKeyboardMarkup()
    water = InlineKeyboardButton("Полить урожай", callback_data="water_plants")
    harvest = InlineKeyboardButton("Собрать урожай", callback_data="harvest_plants")
    plant_a_crop = InlineKeyboardButton("Посадить урожай", callback_data="plant_a_crop")
    markup.add(water)
    markup.add(harvest)
    markup.add(plant_a_crop)
    level = Plants(message.chat.id, 5, 0)
    if level.ripeness == 0:
        dop1 = "вы пока ничего не посадили!"
    text = (f"Ваш огород:\n"
            f"Количество воды: {level.water}\n"
            f"Спелость: {level.ripeness}, {dop1}\n")
    bot.send_message(message.chat.id, text, reply_markup=markup)
    

# 2. Обработка нажатий на кнопки (callback_data)
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == "water_plants":
        # Отвечаем на callback (чтобы кнопка перестала "думать")
        bot.answer_callback_query(call.id, "Вы полили ваши растения!", show_alert=True)
        level.water += 2
    elif call.data == "harvest_plants":
        bot.answer_callback_query(call.id, "Вы собрали растения!", show_alert=True) # Показ всплывающего окна
    elif call.data == "plant_a_crop":
        bot.answer_callback_query(call.id, "Вы посадили растения!", show_alert=True) # Показ всплывающего окна


bot.infinity_polling()