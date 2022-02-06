from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command("phone"))
async def bot_start(msg: types.Message, state: FSMContext):
    await msg.answer("Telfon nomer kiriting")
    await state.set_state("phone")


@dp.message_handler(state="phone")
async def enter_phone(msg: types.Message, state: FSMContext):
    phone = int(msg.text)
    await db.update_user_phone(phone=phone, telegram_id=msg.from_user.id)
    user = await db.select_user(id=msg.from_user.id)
    await msg.answer(f"Baza yangilandi:\n{user}")
    await state.finish()


@dp.message_handler(Command("username"))
async def bot_start(msg: types.Message, state: FSMContext):
    await msg.answer("User name kiritin")
    await state.set_state("username")


@dp.message_handler(state="username")
async def enter_phone(msg: types.Message, state: FSMContext):
    username = msg.text
    await state.update_data(
        {
            "name": username
        }
    )
    await db.update_user_username(username=username, telegram_id=msg.from_user.id)
    user = await db.select_user(telegram_id=msg.from_user.id)
    print(user)
    print(user["username"])

    await msg.answer(f"Username yangilandi: {user['username']}")
    await state.finish()



