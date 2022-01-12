from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.asosiyKeyboard import menuAsosiy
from keyboards.default.menuKeyboard import menu

from loader import dp


@dp.message_handler(Command("menu"))
async def menu_show(msg: Message):
    await msg.answer("Assalom alaykum!", reply_markup=menu)


@dp.message_handler(text="Ish elon")
async def send_smth(msg: Message):
    await msg.answer("Ish uchun elonlar qabul qilamiz")


@dp.message_handler(text="Asosiy")
async def send_sm(msg: Message):
    await msg.answer("Iltimos quyidagilarni tanlang", reply_markup=menuAsosiy)


@dp.message_handler(text="Kirish")
async def send_sm(msg: Message):
    await msg.answer("https://github.com/asil07", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="boshiga")
async def boshiga(msg: Message):
    await msg.answer("Iltimos quyidagilarni tanlang", reply_markup=menu)



