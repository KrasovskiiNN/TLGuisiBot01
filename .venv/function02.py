import requests
import bs4
from bs4 import BeautifulSoup

zodiac_list_latin_russian = {
        'aries': 'Овен',
        'taurus': 'Телец',
        'gemini': 'Близнецы',
        'cancer': 'Рак',
        'leo': 'Лев',
        'virgo': 'Дева',
        'libra': 'Весы',
        'scorpio': 'Скорпион',
        'sagittarius': 'Стрелец',
        'capricorn': 'Козерог',
        'aquarius': 'Водолей',
        'pisces': 'Рыбы'
    }

zodiac_sign_latin = ''

def echo_one_sign():
        response = requests.get(f'https://horo.mail.ru/prediction/{zodiac_sign_latin}/today')
        soup = BeautifulSoup(response.text, 'html.parser')
        prediction = soup.find('div', class_='article__text').text
        zodiac_sign_russian = zodiac_list_latin_russian[zodiac_sign_latin]

        x = (f"{zodiac_sign_russian}. Гороскоп на сегодня:  \n{prediction}")

        return x
