from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.buy_food import book_keys
from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("dimlama"))
async def send_book(message: types.Message):
    photo_id = "AgACAgUAAxkBAAIKw2HmSVuEGGxBe1apakNG_zd0roY4AAKCsTEbS74xV8506VBi2QqcAQADAgADbQADIwQ"
    caption_txt = "Dimlama shiringina. \n Narxi: 50000 so'm\n" \
                  "<b>Halol restoranlar ro'yhati:</b>\n" \
                  "👍Otash qassob\n😋Uzbegim"
    await message.answer_photo(
        photo_id, caption=caption_txt, reply_markup=book_keys
    )













