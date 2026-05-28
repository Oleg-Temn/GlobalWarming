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

@bot.message_handler(commands=["global_warming"])
def gw(message):
    text = ("♨️Глобальное потепление♨️ — это долгосрочное повышение средней температуры климатической системы Земли🌍, "
            "продолжающееся уже более века💯. По данным Организации Объединенных Наций, "
            "главная причина происходящего — активная деятельность человека👨‍🦰 и так называемый парниковый эффект🧖."
            "Ниже подробно разобраны ключевые аспекты этого явления.\nГлавные причины:\n"
            "1. Антропогенный фактор (деятельность человека👱‍♂️): Сжигание ископаемого топлива🛢 (уголь, нефть, газ), масштабная вырубка лесов🪵 и сельское хозяйство приводят к выделению огромных объемов газов.\n"
            "2. Парниковый эффект🧖: Углекислый газ, метан и закись азота накапливаются в атмосфере🌥, пропуская солнечный свет к Земле, но удерживая тепло🌡, которое планета должна была излучать обратно в космос🌌.\n"
            "Основные последствия для планеты🌏:\n"
            "-- Таяние ледников🧊: Повышение температур приводит к быстрому таянию ледников в Арктике, Антарктиде и горных массивах.\n"
            "-- Повышение уровня моря🌊: Из-за таяния льдов и теплового расширения воды уровень Мирового океана неуклонно растет. Это угрожает затоплением прибрежным зонам и островным государствам.\n"
            "-- Экстремальные погодные явления⛈: Климатические изменения провоцируют учащение аномальных засух🏜, лесных пожаров🔥, разрушительных ураганов🌪 и сильных наводнений💦.\n"
            "Угроза для экосистем и сельского хозяйства🌿:\n"
            "Изменение климата нарушает привычные условия обитания многих видов животных🐸, а также напрямую влияет на продовольственную безопасность🌾, снижая урожайность сельскохозяйственных культур.\n"
            "Что предпринимается в мире:\n"
            "Чтобы не допустить катастрофических изменений климата, большинство стран🇷🇺 мира присоединились к Парижскому соглашению. Его главная цель — удержать рост глобальной средней температуры на отметке. Для этого государства переходят на возобновляемые источники энергии (солнечную☀️, ветровую🌬) и снижают углеродный след. Более подробно ознакомиться с научными данными, прогнозами и способами решения проблемы можно на официальном Портале ООН по изменению климата.")
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help(message):
    text = ("Список команд бота:\n"
            "/global_warming -- Описание глобального потепления\n"
            "/random_fact -- Случайный факт про глобальное потепление\n"
            "/start_game -- Начать/продолжить мини-игру\n"
            "Телеграмм-бот может нести чушь. Автор не несет ответственности за его слова")
    bot.send_message(message.chat.id, text)

class SinglePlot:
    def __init__(self):
        self.water = 5
        self.ripeness = 0
        self.canGrow = False

class Plants:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.water = 5
        self.ripeness = 0
        self.money = 0
        self.canGrow = False
        self.growth_speed = 1.0
        self.plots = [SinglePlot()] 
        self.last_message_id = None # ID сообщения для автообновления
        self.dop3 = ""
        self.recently_water = False
        self.recently_humidity = 0
        self.recently_index = 0
        self.autowater = False
        self.autowater2 = "Выкл."
        self.autoharvest = False
        self.autoharvest2 = "Выкл."
        self.autoplant = False
        self.autoplant2 = "Выкл."
        
        # Запускаем персональный цикл роста для этого игрока
        self.start_growth_timer()

    def start_growth_timer(self):
        """Расчитывает время на основе скорости и запускает таймер"""
        # Формула ускорения времени: 3600 секунд делим на скорость игрока
        # Для тестов можно заменить 3600 на 10 (тогда базовое время будет 10 сек)
        interval = 3600 / self.growth_speed 
        
        self.timer = threading.Timer(interval, self.player_growth_tick)
        self.timer.daemon = True
        self.timer.start()

    def player_growth_tick(self):
        """Срабатывает индивидуально для этого игрока, когда проходит его 'час'"""
        need_update_ui = False
        
        # Перебираем только грядки этого конкретного игрока
        for plot in self.plots:
            if plot.canGrow:
                plot.water = max(0, plot.water - 1)
                plot.ripeness = plot.ripeness + 1 # Прибавляем ровно 1 стадию
                if self.autowater2 == "Вкл.":
                    plot.water += 1
                if self.autoharvest2 == "Вкл.":
                    for index, plot in enumerate(self.plots):
                        if 10 > plot.ripeness >= 8:
                            self.money += 1
                            plot.canGrow = False
                            plot.ripeness = 0
                            plot.water = 5
                            if self.autoplant2 == "Вкл.":
                                plot.canGrow = True
                                plot.ripeness = 1
                        elif plot.ripeness >= 10:
                            plot.canGrow = False
                            plot.ripeness = 0
                            plot.water = 5
                            if self.autoplant2 == "Вкл.":
                                plot.canGrow = True
                                plot.ripeness = 1
                need_update_ui = True
                
        # Обновляем сообщение в Телеграм, если что-то выросло
        if need_update_ui and self.last_message_id:
            try:
                bot.edit_message_text(
                    chat_id=self.chat_id,
                    message_id=self.last_message_id,
                    text=get_game_text(self),
                    reply_markup=get_main_keyboard(self)
                )
            except Exception:
                pass
                
        # Перезапускаем таймер на следующий цикл с учетом СВЕЖЕЙ скорости!
        self.start_growth_timer()


players = {}

def get_main_keyboard(game):
    markup = InlineKeyboardMarkup()
    for index, plot in enumerate(game.plots):
        btn_water = InlineKeyboardButton(f"💧 Полить ({plot.water})", callback_data=f"water_{index}")
        btn_plant = InlineKeyboardButton(f"🪏 Посадить ", callback_data=f"plant_{index}")
        btn_harvest = InlineKeyboardButton(f"🍃 Собрать ({plot.ripeness})", callback_data=f"harvest_{index}")
        # Объединяем их в один горизонтальный ряд
        markup.row(btn_water, btn_plant, btn_harvest)
    if game.autowater == True:
        markup.add(InlineKeyboardButton(f"🫙Автополив: {game.autowater2}", callback_data="autowater2"))
    if game.autoharvest == True:
        markup.add(InlineKeyboardButton(f"👨‍🌾Автосборщик: {game.autoharvest2}", callback_data="autoharvest2"))
    if game.autoplant == True:
        markup.add(InlineKeyboardButton(f"✨Автопосадка: {game.autoplant2}", callback_data="autoplant2"))
    markup.add(InlineKeyboardButton("🏪 Магазин", callback_data="shop"))
    return markup

def get_game_text(game):
    if game.recently_water == True:
        game.dop3 = f"💦 Одна грядка полита! [Влажность:{game.recently_humidity}, Номер:{game.recently_index}]"
        
    return (f"Ваш огород:\n"
            f"🪙 Монеты: {game.money}\n"
            f"{game.dop3}")

markup = None

@bot.message_handler(commands=["start_game"])
def start_game(message):
    chat_id = message.chat.id
    if chat_id in players:
        # возвращаем пользователя в огород
        game = players[chat_id]
        bot.send_message(chat_id, "Вы вернулись в свой огород! Игра продолжается.")
    else:
        # Создаем огород конкретного пользователя
        players[chat_id] = Plants(chat_id)

    game = players[chat_id]
    # Создаем клавиатуру
    markup = get_main_keyboard(game)
    
    text = get_game_text(game)
    sent_msg = bot.send_message(chat_id, text, reply_markup=markup)
    game.last_message_id = sent_msg.message_id
    

# 2. Обработка нажатий на кнопки (callback_data)
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    chat_id = call.message.chat.id
    
    # Проверяем, зарегистрирован ли игрок. Если нет — создаем ему игру
    if chat_id not in players:
        players[chat_id] = Plants(chat_id)
        
    game = players[chat_id]

    if "_" in call.data:
        # Разделяем строку: "water_1" превратится в action = "water", index_str = "1"
        action, index_str = call.data.split("_")
        index = int(index_str)
    
        # Берем нужную грядку из списка игрока по её индексу
        current_plot = game.plots[index]
    
        if action == "water":
            current_plot.water = current_plot.water + 1
            bot.answer_callback_query(call.id, f"Грядка №{index+1} полита! 💧")
            game.recently_water = True
            game.recently_humidity = current_plot.water
            game.recently_index = index + 1
            if current_plot.water >= 10:
                current_plot.ripeness = 0
                current_plot.water = 5
                current_plot.canGrow = False
            try:
                bot.edit_message_text(
                    chat_id=game.chat_id,
                    message_id=game.last_message_id,
                    text=get_game_text(game),
                    reply_markup=get_main_keyboard(game)
                )
            except Exception:
                pass
        elif action == "harvest":
            if 7 < current_plot.ripeness < 10:
                game.money += 1
                current_plot.water = 5
                current_plot.ripeness = 0
                current_plot.canGrow = False
                bot.answer_callback_query(call.id, f"Вы получили монету")
            else:
                current_plot.water = 5
                current_plot.ripeness = 0
                current_plot.canGrow = False
                bot.answer_callback_query(call.id, f"Вы собрали урожай не вовремя")
            if game.autoplant2 == "Вкл.":
                current_plot.canGrow = True
                current_plot.ripeness = 1
        elif action == "plant":
            if current_plot.canGrow == False:
                current_plot.canGrow = True
                current_plot.ripeness = 1
                bot.answer_callback_query(call.id, f"Вы засадили грядку!")
            else:
                bot.answer_callback_query(call.id, f"Грядка занята!")

    

    elif call.data == "shop":

        bot.answer_callback_query(call.id, "Вы зашли в магазин!")
        shop_markup = InlineKeyboardMarkup()
        shop_markup.add(InlineKeyboardButton(f"🪴 Приобрести одну грядку({5 * len(game.plots)})", callback_data="new-bed"))
        shop_markup.add(InlineKeyboardButton(f"🧪 Приобрести ускоритель роста({10 * round(game.growth_speed, 1)})", callback_data="boost"))
        if game.autowater == False:
            shop_markup.add(InlineKeyboardButton(f"🧃 Приобрести автополив(10)", callback_data="auto-water"))
        if game.autoharvest == False:
            shop_markup.add(InlineKeyboardButton(f"👨‍🌾 Купить автосборщик(50)", callback_data="auto-harvest"))
        if game.autoplant == False:
            shop_markup.add(InlineKeyboardButton(f"✨ Купить автосеятель(25)", callback_data="auto-plant"))
        shop_markup.add(InlineKeyboardButton("⬅️ Назад", callback_data="back"))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text=f"🏪 Магазин улучшений\n\n💰 Ваш баланс: {game.money} руб.\n\nЧто желаете приобрести?",
            reply_markup=shop_markup
        )
        return


    elif call.data == "back":
        markup = get_main_keyboard(game)

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text=get_game_text(game),
            reply_markup=markup
        )
        return
    

    elif call.data == "new-bed":
        cost = len(game.plots) * 5
        if game.money >= cost:
            game.money -= cost
            game.plots.append(SinglePlot())
            alert = f"Успешно куплена грядка №{len(game.plots)}! 🎉"
        else:
            alert = f"Недостаточно монет! Нужно еще {cost - game.money}"
        bot.answer_callback_query(call.id, alert, show_alert=True)
    

    elif call.data == "boost":
        cost = game.growth_speed * 10
        if game.money >= cost:
            game.money -= cost
            game.growth_speed += game.growth_speed / 10
            alert = f"Успешно куплен ускоритель! Скорость роста теперь {game.growth_speed}! 🎉"
        else:
            alert = f"Недостаточно монет! Нужно еше {cost - game.money}"
        bot.answer_callback_query(call.id, alert, show_alert=True)
    

    elif call.data == "auto-water":
        cost = 10
        if game.money >= cost:
            game.money -= cost
            game.autowater = True
            alert = f"Успешно куплен автополив! Теперь каждый раз огород будет полит автоматически"
            game.autowater2 = "Вкл."
        else:
            alert = f"Недостаточно монет! Нужно еще {cost - game.money}"
        bot.answer_callback_query(call.id, alert, show_alert=True)
    

    elif call.data == "autowater2":
        if game.autowater2 == "Выкл.":
            game.autowater2 = "Вкл."
        elif game.autowater2 == "Вкл.":
            game.autowater2 = "Выкл."
    

    elif call.data == "auto-harvest":
        cost = 50
        if game.money >= cost:
            game.money -= cost
            game.autoharvest = True
            game.autoharvest2 = "Вкл."
            alert = f"Успешно куплен автосборщик! Теперь ваш урожай будет автоматически собран по готовности"
        else:
            alert = f"Нехватает монет! Нужно еще {cost - game.money}"
        bot.answer_callback_query(call.id, alert, show_alert=True)
    

    elif call.data == "autoharvest2":
        if game.autoharvest2 == "Выкл.":
            game.autoharvest2 = "Вкл."
        elif game.autoharvest2 == "Вкл.":
            game.autoharvest2 = "Выкл."
    

    elif call.data == "auto-plant":
        cost = 25
        if game.money >= cost:
            game.money -= cost
            game.autoplant = True
            game.autoplant2 = "Вкл."
            alert = f"Успешно куплен автосеятель! Теперь ваш урожай будет автоматически посеян по свободе грядки"
        else:
            alert = f"Нехватает монет! Нужно еще {cost - game.money}"


    elif call.data == "autoplant2":
        if game.autoplant2 == "Выкл.":
            game.autoplant2 = "Вкл."
        elif game.autoplant2 == "Вкл.":
            game.autoplant2 = "Выкл."
    # После любого действия обновляем текст сообщения интерфейса
    try:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text=get_game_text(game),
            reply_markup=get_main_keyboard(game)
        )
    except telebot.apihelper.ApiTelegramException as e:
        # Игнорируем ошибку, если текст сообщения не изменился, чтобы бот не падал
        if "message is not modified" not in str(e):
            raise e
SAVE_FILE = "players_save.json"

def save_all_players():
    """Конвертирует объекты игроков и их бесконечные грядки в JSON-файл"""
    data_to_save = {}
    
    # 1. Сначала перебираем всех игроков
    for chat_id, game in players.items():
        # 2. Для каждого игрока создаем СВОЙ список грядок
        player_plots = []
        for plot in game.plots:
            # Просто сохраняем параметры грядки в виде словаря
            player_plots.append({
                "water": plot.water,
                "ripeness": plot.ripeness,
                "canGrow": plot.canGrow
            })
            
        # 3. Собираем все данные игрока вместе
        data_to_save[str(chat_id)] = {
            "money": game.money,
            "growth_speed": game.growth_speed,
            "plots": player_plots,  # Сохраняем готовый список словарей грядок
            "autowater": game.autowater,
            "autowater2": game.autowater2,
            "autoharvest": game.autoharvest,
            "autoharvest2": game.autoharvest2,
            "autoplant": game.autoplant,
            "autoplant2": game.autoplant2
        }
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    print("💾 Автосохранение успешно выполнено!")


def load_all_players():
    """Загружает данные игроков и восстанавливает список их грядок"""
    global players
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                for chat_id_str, stats in data.items():
                    chat_id = int(chat_id_str)
                    
                    # Создаем объект игрока
                    game = Plants(chat_id)
                    game.money = stats.get("money", 0)
                    game.growth_speed = stats.get("growth_speed", 1.0)
                    game.autowater = stats.get("autowater", False)
                    game.autowater2 = stats.get("autowater2", "Выкл.")
                    game.autoharvest = stats.get("autoharvest", False)
                    game.autoharvest2 = stats.get("autoharvest2", "Выкл.")
                    game.autoplant = stats.get("autoplant", False)
                    game.autoplant2 = stats.get("autoplant2", "Выкл.")
                    
                    # Очищаем дефолтную грядку, созданную при старте класса, 
                    # чтобы загрузить точное количество из файла
                    game.plots = []
                    
                    # Восстанавливаем каждую грядку из сохраненного списка
                    saved_plots = stats.get("plots", [])
                    for plot_data in saved_plots:
                        # Создаем чистый объект одиночной грядки
                        new_plot = SinglePlot()
                        # Заполняем его сохраненными параметрами
                        new_plot.water = int(plot_data["water"])
                        new_plot.ripeness = float(plot_data["ripeness"])
                        new_plot.canGrow = bool(plot_data["canGrow"])
                        
                        # Добавляем восстановленную грядку в список игрока
                        game.plots.append(new_plot)
                        
                    # Сохраняем игрока со всеми его грядками в общий словарь
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

def set_bot_commands():
    try:
        commands = [
            telebot.types.BotCommand("start_game", "🏡 Открыть огород / Начать игру"),
            telebot.types.BotCommand("random_fact", "⁉️Случайный факт о глобальном потеплении"),
            telebot.types.BotCommand("global_warming", "♨️Что такое глобальное потепление"),
            telebot.types.BotCommand("help", "❓ Показать инструкцию и помощь")
        ]
        bot.set_my_commands(commands)
        print("✅ Подсказки команд успешно загружены в Telegram!")
    except Exception as e:
        print(f"⚠️ Не удалось загрузить подсказки: {e}")

set_bot_commands()

bot.infinity_polling()