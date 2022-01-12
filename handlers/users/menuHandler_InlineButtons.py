import logging


from aiogram.types import Message, CallbackQuery
from keyboards.inline.productsKeyboard import categoryMenu, taomlarMenu
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(msg: Message):
    await msg.answer("Mahsulotlarni tanlang", reply_markup=categoryMenu)


@dp.callback_query_handler(text="taomlar")
async def buy_food(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.delete()
    await call.message.answer("Taomni tanlang", reply_markup=taomlarMenu)
    await call.answer(cache_time=60)



