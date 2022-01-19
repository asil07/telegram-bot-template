from aiogram.types import CallbackQuery

from loader import dp, bot


@dp.callback_query_handler(text="rasm", )
async def send_info(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text="Batafsil zorrrrrr")
    await call.answer(cache_time=60)