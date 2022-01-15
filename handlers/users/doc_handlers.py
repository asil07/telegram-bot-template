from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download()
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")


# @dp.message_handler(content_types=ContentType.VIDEO)
@dp.message_handler(content_types='video')
async def video_handler(message: Message):
    await message.video.download()
    await message.reply("Video qabul qilindi\n"
                    f"file_id = {message.video.file_id}")





