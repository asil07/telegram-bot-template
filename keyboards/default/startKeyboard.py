from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar 🛍"),
            KeyboardButton(text="Xizmatlar 📥")
        ],
    ],
    resize_keyboard=True
)
