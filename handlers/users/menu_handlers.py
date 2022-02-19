from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboards import (menu_callbackdata, categories_keyboard,
                                             subcategories_keyboard, items_keyboard, item_keyboard)

from loader import dp, db


@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_categories(message)


# KAtegoriyalrni qaytaruvchi funksiya Callback ham Message ham qabul qilishi va boshqa **kwargs
# parametrlarini qabul qilishi mumkn
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, Message):
        await message.answer("Bo'limni tanlang", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# Ost kategoriyal
async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    await callback.message.edit_reply_markup(markup)


# mahsulotlar royhati
async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    await callback.message.edit_text(text="Mahsulotni Tanlang", reply_markup=markup)


# mahsullotni ko'rsatish
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    item = await db.get_product(item_id)

    if item["photo"]:
        text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
    else:
        text = f"{item['productname']}\n\n"

    text += f"Narxi: {item['price']}$\n{item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


# Barch funksiyalar u/n yagona handler
@dp.callback_query_handler(menu_callbackdata.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
        :param call: Handlerga kelgan Callback query
        :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """
    current_level = callback_data.get("level")

    # foydalanuvchi so'ragan kategoriya
    category = callback_data.get("category")

    # soralgan subcategoriya
    subcategory = callback_data.get("subcategory")

    # id raqam
    item_id = int(callback_data.get("item_id"))

    # har bir levelga mos categoriyalar

    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
        "2": list_items,  # Mahsulotlarni qaytaramiz
        "3": show_item,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )
