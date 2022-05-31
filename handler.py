import telebot
# pyTelegramBotAPI	4.3.1
from telebot import types
from conf import bot_token #выдернул токен из файла
from conf import weather_token
import requests # Требуется для "Прислать собаку"
import bs4 # требуется для get_anekdot()

bot = telebot.TeleBot(bot_token)  # Создаем экземпляр бота

def get_anekdot():  #вытаскиваем анекдот с сайта
    array_anekdots = []
    s = requests.get('https://nekdo.ru/random/')
    soup = bs4.BeautifulSoup(s.text, "html.parser")
    result_find = soup.select('.text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

#def get_anime():  #вытаскиваем тайтл с сайта (ps не вытаскиваем, сайт не даёт название)
    #array_anime = []
    #s = requests.get('https://anime777.ru/random/')
    #soup = bs4.BeautifulSoup(s.text, "html.parser")
    #result_find = soup.select('.text')
    #for result in result_find:
     #   array_anime.append(result.getText().strip())
    #return array_anime[0]

def dz_1():
    name = "roma"
    return name
def dz_2():
    age = 17
    name = "roma"
    c = ('my name is roma and im 18')
    return c

#https://anime777.ru/random