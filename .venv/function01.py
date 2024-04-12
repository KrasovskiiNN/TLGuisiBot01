import requests
import bs4
from bs4 import BeautifulSoup

def echo_all():
    x = requests.get('https://horo.mail.ru/')
    y = bs4.BeautifulSoup(x.text, 'html.parser')
    z = ''

    horoText = y.select('.article__text')

    for a in horoText:
        x = (a.getText().strip())
        z = z + x +'\n\n'

    return x
