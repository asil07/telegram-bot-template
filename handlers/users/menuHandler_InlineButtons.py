import logging


from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_data import ichimliklar_callback, taomlar_callback
from keyboards.inline.productsKeyboard import categoryMenu, taomlarMenu, ichimlik_Menu, cola_keyboard
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(msg: Message):
    await msg.answer("Mahsulotlarni tanlang", reply_markup=categoryMenu)


@dp.callback_query_handler(text="ortga")
async def go_back(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")

    await call.message.edit_reply_markup(reply_markup=categoryMenu)

    # await call.message.answer("Iltimos tanlangchi!", reply_markup=categoryMenu)


@dp.callback_query_handler(text="taomlar")
async def buy_food(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.delete()
    await call.message.answer("Taomni tanlang", reply_markup=taomlarMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="ichimlik")
async def buy_drinks(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.delete()
    await call.message.answer("Ichimliklarni tanlang", reply_markup=ichimlik_Menu)
    await call.answer(cache_time=60)


# callback filter
@dp.callback_query_handler(ichimliklar_callback.filter(item_name="cola"))
async def buying_cola(call: CallbackQuery, callback_data: dict):

    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer("Siz cola sotib olmoqchimisz?",
                              reply_markup=cola_keyboard)

    await call.answer(cache_time=60)


@dp.callback_query_handler(taomlar_callback.filter(item_name="palov"))
async def buying_palov(call: CallbackQuery, callback_data: dict):
    logging.info(f'{callback_data=}')

    await call.answer("Buyurtma qabul qilindi", cache_time=60, show_alert=True)


