from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback



coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)


categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
        InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
    ],
    [
        InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram"),
    ],
    [
        InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
    ],
    [
        InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"),
    ],
])









