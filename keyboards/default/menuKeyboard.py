from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy"),
            KeyboardButton(text="Ish elon")
        ],
    ],
    resize_keyboard=True
)
