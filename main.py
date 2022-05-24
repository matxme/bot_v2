
import telebot
# pyTelegramBotAPI	4.3.1
from telebot import types
from conf import bot_token #выдернул токен из файла
from conf import weather_token #токен для парсинга погоды
import requests # Требуется для "Прислать собаку"
import bs4 # требуется для get_anekdot()
from handler import get_anekdot
from handler import get_weather
from handler import dz_1
from handler import dz_2
import game


bot = telebot.TeleBot(bot_token)  # Создаем экземпляр бота

#получение разных файлов
@bot.message_handler(content_types=['sticker'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This is " + message.content_type)

    sticker = message.sticker
    bot.send_message(message.chat.id, sticker)

@bot.message_handler(content_types=['audio'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This is " + message.content_type)

    audio = message.audio
    bot.send_message(chat_id, audio)

@bot.message_handler(content_types=['voice'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This is " + message.content_type)

    voice = message.voice
    bot.send_message(message.chat.id, voice)

@bot.message_handler(content_types=['photo'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This is " + message.content_type)

    photo = message.photo
    bot.send_message(message.chat.id, photo)

@bot.message_handler(content_types=['video'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "This is " + message.content_type)

    video = message.video
    bot.send_message(message.chat.id, video)

# Получение документов от юзера
@bot.message_handler(content_types=['document'])
def get_messages(message):
    chat_id = message.chat.id
    mime_type = message.document.mime_type
    bot.send_message(chat_id, "This is " + message.content_type + " (" + mime_type + ")")

    document = message.document
    bot.send_message(message.chat.id, document)
    if message.document.mime_type == "video/mp4":
        bot.send_message(message.chat.id, "This is a GIF!")

@bot.message_handler(commands=["start"]) #стартовое сообщение
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Main menu")
    btn2 = types.KeyboardButton("Help")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="how do u feel {0.first_name}? im testing bot".format(
                         message.from_user), reply_markup=markup)


# Получение разных сценариев от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "Main menu" or ms_text == "Back to menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Some gags")
        btn2 = types.KeyboardButton("Game")
        btn3 = types.KeyboardButton("Settings")
        btn4 = types.KeyboardButton("DZ")
        back = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="That is a main menu", reply_markup=markup)

    elif ms_text == "DZ" or ms_text == "ДЗ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("full code")
        btn1 = types.KeyboardButton("dz_1")
        btn2 = types.KeyboardButton("dz_2")
        btn3 = types.KeyboardButton("dz_3")
        btn4 = types.KeyboardButton("dz_4")
        btn5 = types.KeyboardButton("dz_5")
        btn6 = types.KeyboardButton("dz_6")
        back = types.KeyboardButton("Back to menu")
        markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(chat_id, text="This is gags menu", reply_markup=markup)

    elif ms_text == "Some gags":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("random dog")
        btn2 = types.KeyboardButton("get gag")
        back = types.KeyboardButton("Back to menu")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="This is gags menu", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "random dog":
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="lol, that ur good boy")

    elif ms_text == "get gag":
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "Game":
        #game21 = botGames.getGame(chat_id)
        bot.send_message(chat_id, text='bruh... i tired')


    elif ms_text == "Settings":
        bot.send_message(chat_id, text="not ready")

    elif ms_text == "Help" or ms_text == "/help":
        bot.send_message(chat_id, "by matome \nfor ask: \n@matxme")

    elif ms_text == "dz_1":
        bot.send_message(chat_id, text=dz_1())

    elif ms_text == "dz_2":
        bot.send_message(chat_id, text=dz_2())

    elif ms_text == "full code":
        bot.send_message(chat_id, text='https://github.com/matxme/lab1.py/blob/master/lab1.py')

    else:
        bot.send_message(chat_id, text="yep..." + ms_text)

bot.polling(none_stop=True, interval=0) # Запускаем бота

print()











