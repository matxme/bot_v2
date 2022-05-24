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
    z = ''
    s = requests.get('https://nekdo.ru/random/')
    soup = bs4.BeautifulSoup(s.text, "html.parser")
    result_find = soup.select('.text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

def get_weather(city, tok):  #вытаскиваем погоду с сайта
    city = input('Введите название города')
    tok = weather_token
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tok}')
    data = r.json()
    print (data)

def dz_1():
    name = "roma"
    return name
def dz_2():
    age = 17
    name = "roma"
    c = ('my name is', name, 'and im', age)
    return c
