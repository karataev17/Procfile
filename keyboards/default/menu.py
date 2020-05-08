from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сколько мне надо набрать на сессии?"),
        ],

        [
            KeyboardButton(text="Лек/практика/сро"),
        ],
        [
            KeyboardButton(text="Практика/Сро"),

        ],
        [
            KeyboardButton(text="Лек/Сро/Лабка"),

        ],
        [
            KeyboardButton(text="Лек/практика/сро/лабка"),
        ],
    ],
    resize_keyboard=True
)