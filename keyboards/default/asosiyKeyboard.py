from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAsosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kirish"),
            KeyboardButton(text="darsalar"),
            KeyboardButton(text="Taxsi buyurtma")
        ],
        [
            KeyboardButton(text="ortga"),
            KeyboardButton(text="boshiga")
        ]
    ],
    resize_keyboard=True
)
