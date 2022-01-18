from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.templates import coursesMenu, categoryMenu
from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)



@dp.message_handler(Command("dimlama"))
async def send_book(message: types.Message):
    photo_id = "AgACAgUAAxkBAAIKw2HmSVuEGGxBe1apakNG_zd0roY4AAKCsTEbS74xV8506VBi2QqcAQADAgADbQADIwQ"
    # photo_url = "https://images.unsplash.com/photo-1576872381149-7847515ce5d8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80"
    # photo_file = InputFile(path_or_bytesio="photos/kitob.jpg")
    # await message.reply_photo(
    #     photo_file, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
    # )
    await message.answer_photo(
        photo_id, caption="Dimlama shiringina. \n Narxi: 50000 so'm"
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_id,
        caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm",
    )


@dp.message_handler(Command("resumelar"))
async def send_templates(msg: types.Message):
    album = types.MediaGroup()
    photo_1 = "AgACAgUAAxkBAAIKw2HmSVuEGGxBe1apakNG_zd0roY4AAKCsTEbS74xV8506VBi2QqcAQADAgADbQADIwQ"
    photo_2 = "AgACAgUAAxkBAAIKsmHmR0GtV8D2mKRuXSzDQzi5hsV4AAJ2sTEbS74xV79O0Q0-G-cwAQADAgADeQADIwQ"
    photo_3 = "AgACAgUAAxkBAAIKzmHmSvKU3ov3eOn_xlcrmR9kQ2GNAAL6sDEbS74xV7RXdagAAczeqQEAAwIAA3gAAyME"
    video = "BAACAgUAAxkBAAIK0GHmS1u4TQs38dPrz0mH2pismSsiAAJwBAACxEp4VRanlSfQE3Q6IwQ"

    album.attach_photo(photo=photo_1)
    album.attach_photo(photo=photo_2)
    album.attach_photo(photo=photo_3)
    album.attach_video(video=video, caption="Clubhouse")

    await msg.reply_media_group(media=album)
    await msg.answer("Iltimos tanlang", reply_markup=categoryMenu)










