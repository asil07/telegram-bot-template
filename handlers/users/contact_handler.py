from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.contact_button import keyboard
from loader import dp


@dp.callback_query_handler(text="mycontact")
async def send_contact(call: CallbackQuery):
    await call.message.answer("Kontakt yuboring", reply_markup=keyboard)


@dp.message_handler(content_types="contact")
async def get_cnt(msg: Message):
    contact = msg.contact
    await msg.answer(f'Rahmat {contact.full_name}\n'
                     f'Sizning {contact.phone_number} raqamingiz qabul qilindi',
                     reply_markup=ReplyKeyboardRemove())


