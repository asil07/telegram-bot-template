import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)


    await message.answer(f"Salom, {message.from_user.full_name}! Xush kelibsiz")

    # Notify Admins
    count = await db.count_users()
    msg = f"{user[1]} nomli user bazaga qo'shildi.\nJami bazada {count}ta userlar bor"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
