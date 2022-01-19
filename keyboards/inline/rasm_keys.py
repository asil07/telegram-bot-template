from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


keybord = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Zor👍", callback_data="rasm"),
        InlineKeyboardButton(text="rasmni korisih", url="https://images.unsplash.com/photo-1589254065909-b7086229d08c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cm9ib3R8ZW58MHx8MHx8&auto=format&fit=crop&w=900&q=60")
    ],
    [
        InlineKeyboardButton(text="Ulashish", switch_inline_query="valli")
    ]
])

artificial = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Zor👍", callback_data="rasm"),
        InlineKeyboardButton(text="rasmni korisih", url="https://images.unsplash.com/photo-1599790772272-d1425cd3242e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHJvYm90fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60")
    ],
    [
        InlineKeyboardButton(text="Ulashish", switch_inline_query="artficial")
    ]
])