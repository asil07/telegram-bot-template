from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1 - usul
from keyboards.inline.callback_data import taomlar_callback, ichimliklar_callback

categoryMenu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Taomlar", callback_data="taomlar"),
        InlineKeyboardButton(text="Ichimliklar", callback_data="ichimlik")
    ],
    [
        InlineKeyboardButton(text="Oshxona Sahifasiga o'tish", url="https://korzinka.uz/uz/")
    ],
    [
        InlineKeyboardButton(text="🔦 Qidiruv", switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text="🗣 Ulashish", switch_inline_query="Milliy taomlar")
    ]
])


# 2 - usul
taomlarMenu = InlineKeyboardMarkup(row_width=2)
dimlama = InlineKeyboardButton(text="Dimalama 😋",
                              callback_data=taomlar_callback.new(item_name="dimlama"))
taomlarMenu.insert(dimlama)

osh = InlineKeyboardButton(text="Palovxon to'ra",
                           callback_data=taomlar_callback.new(item_name="palov"))
taomlarMenu.insert(osh)

mastava = InlineKeyboardButton(text="Mastava", callback_data="taomlar:mastava")
taomlarMenu.insert(mastava)

shorva = InlineKeyboardButton(text="Sho'rva", callback_data="taomlar: shorva")
taomlarMenu.insert(shorva)

ortga = InlineKeyboardButton(text="Ortga", callback_data="ortga")
taomlarMenu.insert(ortga)


# 3 - usul

ichimliklar = {
    "Coca-Cola": "cola",
    "Fanta": "fanta",
    "Ko'k choy": "choy",

}

ichimlik_Menu = InlineKeyboardMarkup(row_width=2)

for key, value in ichimliklar.items():
    ichimlik_Menu.insert(InlineKeyboardButton(text=f"{key}",
                                              callback_data=ichimliklar_callback.new(value)))
ichimlik_Menu.insert(ortga)

# har bir ichimlik uchun tugma
cola_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/"),
        InlineKeyboardButton(text="savatga qo'shish", callback_data="ichimlik")
    ]
])

algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
    ]
])


