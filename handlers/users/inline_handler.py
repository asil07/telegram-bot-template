from aiogram import types

from data.datas_shop import inline_query_product
from keyboards.inline.rasm_keys import keybord, artificial
from loader import dp

# for sikl da yaratish
@dp.inline_handler(text="taom")
async def send_taom(query: types.InlineQuery):
    await query.answer(inline_query_product)


# Rasmlar bilan iishlash👇
@dp.inline_handler(text='robot')
async def photo(query: types.InlineQuery):
    await query.answer(results=[
        types.InlineQueryResultPhoto(
            id="r112",
            photo_url="https://images.unsplash.com/photo-1589254065909-b7086229d08c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cm9ib3R8ZW58MHx8MHx8&auto=format&fit=crop&w=900&q=60",
            thumb_url="https://images.unsplash.com/photo-1589254065909-b7086229d08c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cm9ib3R8ZW58MHx8MHx8&auto=format&fit=crop&w=900&q=60",
            caption="VAlli multfilmi",
            reply_markup=keybord
        ),
        types.InlineQueryResultPhoto(
            id="r113",
            photo_url="https://images.unsplash.com/photo-1599790772272-d1425cd3242e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHJvYm90fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
            thumb_url="https://images.unsplash.com/photo-1599790772272-d1425cd3242e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHJvYm90fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
            caption="Artificial robot",
            reply_markup=artificial
        ),
        types.InlineQueryResultVideo(
            id="r111",
            video_url="https://youtu.be/2Giu6Hr4M9c",
            thumb_url="https://images.unsplash.com/photo-1599790772272-d1425cd3242e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHJvYm90fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
            caption="Domla",
            description="Xayot mazmuni",
            title="Milliy",
            mime_type="video/mp4"

        )

    ])


@dp.inline_handler()
async def emty_query(query: types.InlineQuery):
    await query.answer(results=[
        types.InlineQueryResultArticle(
            id="kurs007",
            title="Kafeyimiz ovqatlari",
            input_message_content=types.InputTextMessageContent(
                message_text="Git hub profil link : https://github.com/asil07"),
            url="https://github.com/asil07",
            thumb_url="https://images.unsplash.com/photo-1642348021424-848cc045b667?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1696&q=80",
            description="Github descriptionga yozilgan matn"
        ),
        types.InlineQueryResultArticle(
            id="kurs003",
            title="Kafeyimiz ovqatlari",
            input_message_content=types.InputTextMessageContent(
                message_text="Git hub profil link : https://github.com/asil07"),
            url="https://github.com/asil07",
            thumb_url="https://images.unsplash.com/photo-1642348021424-848cc045b667?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1696&q=80",
            description="Github descriptionga yozilgan matn"
        ),
        types.InlineQueryResultArticle(
            id="kurs004",
            title="Kafeyimiz ovqatlari",
            input_message_content=types.InputTextMessageContent(
                message_text="Git hub profil link : https://github.com/asil07"),
            url="https://github.com/asil07",
            thumb_url="https://avatars.githubusercontent.com/u/78051772?v=4",
            description="Github descriptionga yozilgan matn"
        ),
    ])