# импорт используемых библиотек

import keyboard01
import telebot
import requests
import bs4

# импорт файлов проекта (отдельно вынесенные блоки кода)

import config
import function01
import function02
import keyboard01

from telebot import types
from requests import get

# токен бота для безопасности вынесен в отдельный файл

botHoroMailRu = telebot.TeleBot(config.Bot_API_Token)

# Хэндлер-обработчик команды /start - приветствие пользователя и вывод общего гороскопа на текущий день.
# Функция вывода общего гороскопа на текущий день - парсер импортированный из function01

@botHoroMailRu.message_handler(commands=['start'])
def startBot(message):
    start_mess_1 = f'Добрый день <em>{message.from_user.first_name}</em>!'
    start_mess_2 = f'<u><b>Гороскоп для всех знаков на сегодня:</b></u>'
    botHoroMailRu.send_message(message.chat.id, start_mess_1, parse_mode='html')
    botHoroMailRu.send_message(message.chat.id, start_mess_2, parse_mode='html')
    botHoroMailRu.send_message(message.chat.id, function01.echo_all())

    start_mess_3 = f'<u><b>Выберите знак зодиака:</b></u>'
    botHoroMailRu.send_message(message.chat.id, start_mess_3, parse_mode='html', reply_markup=keyboard01.keyboard)

# Хэндлер-обработчик вызова нажатия кнопки
# Функция вывода индидвидуального гороскопа на текущий день - парсер импортированный из function02

@botHoroMailRu.callback_query_handler(func=lambda callback: True)
def signZodiac(callback):
    if callback.data == 'aries':
        function02.zodiac_sign_latin = 'aries'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'taurus':
        function02.zodiac_sign_latin = 'taurus'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'gemini':
        function02.zodiac_sign_latin = 'gemini'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'cancer':
        function02.zodiac_sign_latin = 'cancer'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'leo':
        function02.zodiac_sign_latin = 'leo'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'virgo':
        function02.zodiac_sign_latin = 'virgo'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'libra':
        function02.zodiac_sign_latin = 'libra'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'scorpio':
        function02.zodiac_sign_latin = 'scorpio'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'sagittarius':
        function02.zodiac_sign_latin = 'sagittarius'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'capricorn':
        function02.zodiac_sign_latin = 'capricorn'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'aquarius':
        function02.zodiac_sign_latin = 'aquarius'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())
    elif callback.data == 'pisces':
        function02.zodiac_sign_latin = 'pisces'
        botHoroMailRu.send_message(callback.message.chat.id, function02.echo_one_sign())

botHoroMailRu.polling(non_stop=True)