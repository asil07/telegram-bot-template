from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode

from keyboards.default import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.callback_query_handler(text="mylocation")
async def show_location(call: CallbackQuery):
    await call.message.answer(text="Lokatsiya yuboring", reply_markup=keyboard)


@dp.message_handler(content_types="location")
async def get_loc(msg: Message):
    location = msg.location
    lat = location.latitude
    lon = location.longitude
    closest_one = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n"
                        f"Masofa: {distance:.1f}"
                        for shop_name, distance, url, shop_location in closest_one])
    await msg.answer(f"Marhamat\n"
                     f"Latitude: {lat}\n"
                     f"Lon: {lon}\n\n"
                     f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove()
                     )

    for shop_name, distance, url, shop_location in closest_one:
        await msg.answer_location(latitude=shop_location["lat"], longitude=shop_location["lon"])









