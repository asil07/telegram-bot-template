from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/all", user_id=ADMINS)
async def get_all(msg: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    print(users[0][1])
    await msg.answer(users)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ads(msg: types.Message):
    users = db.select_all_users()

    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Assalomu alaykum")


@dp.message_handler(text="/tozala", user_id=ADMINS)
async def cleaning_db(msg: types.Message):
    db.delete_users()
    await msg.answer("Baza tozalandi")