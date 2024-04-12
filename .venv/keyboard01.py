import telebot
from telebot import types

# Клавиатура для перехода на выбранный знак Зодиака.

keyboard = types.InlineKeyboardMarkup(row_width=4)

button1 = types.InlineKeyboardButton(text="Овен", callback_data="aries")
button2 = types.InlineKeyboardButton(text="Телец", callback_data="taurus")
button3 = types.InlineKeyboardButton(text="Близнецы", callback_data="gemini")
button4 = types.InlineKeyboardButton(text="Рак", callback_data="cancer")
button5 = types.InlineKeyboardButton(text="Лев", callback_data="leo")
button6 = types.InlineKeyboardButton(text="Дева", callback_data="virgo")
button7 = types.InlineKeyboardButton(text="Весы", callback_data="libra")
button8 = types.InlineKeyboardButton(text="Скорпион", callback_data="scorpio")
button9 = types.InlineKeyboardButton(text="Стрелец", callback_data="sagittarius")
button10 = types.InlineKeyboardButton(text="Козерог", callback_data="capricorn")
button11 = types.InlineKeyboardButton(text="Водолей", callback_data="aquarius")
button12 = types.InlineKeyboardButton(text="Рыбы", callback_data="pisces")

keyboard.add(button1, button2, button3, button4)
keyboard.add(button5, button6, button7, button8)
keyboard.add(button9, button10, button11, button12)
