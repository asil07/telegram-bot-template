import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboard import menu
from keyboards.default.startKeyboard import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.id}")
    logging.info(f"{message.from_user.full_name}")
    await message.answer(f"Salom, {message.from_user.full_name}!\n", reply_markup=menuStart)


