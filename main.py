import telebot
import random
import os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
import time
import json


load_dotenv()
bot = telebot.TeleBot(token=os.getenv('TG_API_TOKEN'))

# Функции с фактами

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
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.water = 5
        self.ripeness = 0
        self.soil = 0
        self.canGrow = False

players = {}

def get_game_text(game):
    if game.ripeness == 0:
        dop1 = "вы пока ничего не посадили!"
    else:
        dop1 = ""
    
    if game.water >= 8:
        dop2 = "уровень воды находится на максимальном уровне!"
    elif game.water <= 2:
        dop2 = "ваш урожай скоро высохнет!"
    else:
        dop2 = ""
        
    return (f"Ваш огород:\n"
            f"Количество воды: {game.water} {dop2}\n"
            f"Спелость: {game.ripeness} {dop1}\n"
            f"Количество удобрений: {game.soil}")


# Фоновый поток для ежечасного обновления параметров грядок
def global_growth_loop():
    while True:
        time.sleep(3600)  # Интервал в 1 час (3600 секунд). Для тестов можно поставить 5-10 секунд.
        for chat_id, game in list(players.items()):
            if game.canGrow:
                game.water = max(0, game.water - 1)
                game.ripeness += 1
                
                # Опционально: можно отправлять уведомление игроку, что грядка изменилась
                try:
                    text = "🌟 Прошел час! Состояние вашего огорода обновилось.\n\n" + get_game_text(game)
                    # Создаем клавиатуру заново для уведомления
                    markup = InlineKeyboardMarkup()
                    markup.add(InlineKeyboardButton("Полить урожай", callback_data="water_plants"))
                    markup.add(InlineKeyboardButton("Собрать урожай", callback_data="harvest_plants"))
                    markup.add(InlineKeyboardButton("Посадить урожай", callback_data="plant_a_crop"))
                    bot.send_message(chat_id, text, reply_markup=markup)
                except Exception as e:
                    print(f"Не удалось отправить уведомление в чат {chat_id}: {e}")

# Запуск фонового процесса роста
growth_thread = threading.Thread(target=global_growth_loop, daemon=True)
growth_thread.start()

markup = None
dop1 = ""
dop2 = ""
dop3 = ""
dop4 = ""


@bot.message_handler(commands=["start_game"])
def start_game(message):
    chat_id = message.chat.id
    
    # Создаем или сбрасываем огород конкретного пользователя
    players[chat_id] = Plants(chat_id)
    game = players[chat_id]

    # Создаем клавиатуру
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Полить урожай", callback_data="water_plants"))
    markup.add(InlineKeyboardButton("Собрать урожай", callback_data="harvest_plants"))
    markup.add(InlineKeyboardButton("Посадить урожай", callback_data="plant_a_crop"))
    
    text = get_game_text(game)
    bot.send_message(chat_id, text, reply_markup=markup)
    

# 2. Обработка нажатий на кнопки (callback_data)
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    chat_id = call.message.chat.id
    
    # Проверяем, зарегистрирован ли игрок. Если нет — создаем ему игру
    if chat_id not in players:
        players[chat_id] = Plants(chat_id)
        
    game = players[chat_id]

    if call.data == "water_plants":
        game.water += random.randint(1, 2)
        bot.answer_callback_query(call.id, "Вы полили ваши растения!", show_alert=True)
        game = players[chat_id]
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,  # ID сообщения, на котором нажали кнопку
            text=get_game_text(game),            # Генерируем новый текст с обновленными dop1/dop2
            reply_markup=call.message.reply_markup # Оставляем те же самые инлайн-кнопки под текстом
        )


    elif call.data == "harvest_plants":
        if 7 < game.ripeness < 10:
            game.soil += 1
            game.ripeness = 0
            game.canGrow = False
            alert_text = "Вы успешно собрали зрелый урожай и получили 1 удобрение!"
        elif game.ripeness >= 10:
            game.ripeness = 0
            game.canGrow = False
            alert_text = "Урожай перезрел и сгнил! Вы всё убрали, грядка пуста."
        else:
            alert_text = "Вы собрали урожай слишком рано! Растения погибли."
            game.ripeness = 0
            game.canGrow = False
            
        bot.answer_callback_query(call.id, alert_text, show_alert=True)
        game = players[chat_id]
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,  # ID сообщения, на котором нажали кнопку
            text=get_game_text(game),            # Генерируем новый текст с обновленными dop1/dop2
            reply_markup=call.message.reply_markup # Оставляем те же самые инлайн-кнопки под текстом
        )


    elif call.data == "plant_a_crop":
        if game.ripeness == 0 and not game.canGrow:
            game.canGrow = True
            game.water = 5  # сбрасываем воду до нормы при посадке
            alert_text = "Вы успешно посадили растения! Теперь они растут."
        else:
            alert_text = "У вас уже что-то растет на грядке!"
            
        bot.answer_callback_query(call.id, alert_text, show_alert=True)
        game = players[chat_id]
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,  # ID сообщения, на котором нажали кнопку
            text=get_game_text(game),            # Генерируем новый текст с обновленными dop1/dop2
            reply_markup=call.message.reply_markup # Оставляем те же самые инлайн-кнопки под текстом
        )
    # После любого действия обновляем текст сообщения интерфейса
    try:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text=get_game_text(game),
            reply_markup=call.message.reply_markup
        )
    except telebot.apihelper.ApiTelegramException as e:
        # Игнорируем ошибку, если текст сообщения не изменился, чтобы бот не падал
        if "message is not modified" not in str(e):
            raise e
SAVE_FILE = "players_save.json"

def save_all_players():
    """Конвертирует объекты игроков в текст и сохраняет в JSON-файл"""
    data_to_save = {}
    for chat_id, game in players.items():
        data_to_save[str(chat_id)] = {
            "water": game.water,
            "ripeness": game.ripeness,
            "soil": game.soil,
            "canGrow": game.canGrow
        }
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    print("💾 Автосохранение успешно выполнено!")

def load_all_players():
    """Загружает данные из файла при старте бота"""
    global players
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for chat_id_str, stats in data.items():
                    chat_id = int(chat_id_str)
                    # Создаем объект игрока и восстанавливаем его параметры
                    game = Plants(chat_id)
                    game.water = stats["water"]
                    game.ripeness = stats["ripeness"]
                    game.soil = stats["soil"]
                    game.canGrow = stats["canGrow"]
                    players[chat_id] = game
            print(f"📂 Успешно загружено игроков из файла: {len(players)}")
        except Exception as e:
            print(f"⚠️ Ошибка при загрузке сохранения: {e}")

def auto_save_loop():
    while True:
        time.sleep(300)  # 300 секунд = 5 минут
        try:
            save_all_players()
        except Exception as e:
            print(f"Ошибка при автосохранении: {e}")

# Запуск потока автосохранения (перед отправкой bot.infinity_polling)
save_thread = threading.Thread(target=auto_save_loop, daemon=True)
save_thread.start()

load_all_players()

bot.infinity_polling()