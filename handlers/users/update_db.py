from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def enter_email(msg: types.Message, state: FSMContext):
    await msg.answer("Email manzil kiriting")
    await state.set_state("email")

@dp.message_handler(state="email")
async def email_entry(msg: types.Message, state:FSMContext):
    db.update_user_email(msg.text, id=msg.from_user.id)
    user = db.select_user(id=msg.from_user.id)
    await msg.answer(f"Baza yangilandi {user}")
    await state.finish()


