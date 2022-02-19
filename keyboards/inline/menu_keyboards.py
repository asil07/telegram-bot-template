import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

menu_callbackdata = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


def make_cd(level, category=0, subcategory=0, item_id=0):
    return menu_callbackdata.new(
        level=level, category=category, subcategory=subcategory, item_id=item_id
    )


# Bizning menu 3 qavat (LEVEL) dan iborat
# 0 - Kategoriyalar
# 1 - Ost-kategoriyalar
# 2 - Mahsulotlar
# 3 - Yagona mahsulot


async def categories_keyboard():
    CURRENT_LEVEL = 0

    markup = InlineKeyboardMarkup(row_width=1)

    categories = await db.get_categories()
    for category in categories:
        number_of_items = await db.count_products(category["category_code"])
        button_text = f"{category['category_name']} ({number_of_items} dona) "

        # tugmanin bosganda qaytuvchi callback

        callback_data = make_cd(
            level=CURRENT_LEVEL + 1, category=category["category_code"]
        )
        logging.info(callback_data)
        # keyboadga qoshamiz
        markup.insert(InlineKeyboardButton(text=button_text, callback_data=callback_data))
    return markup


async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1

    markup = InlineKeyboardMarkup(row_width=1)

    subcategories = await db.get_subcategories(category)
    for subcat in subcategories:
        number_of_items = await db.count_products(category_code=category,
                                                  subcategory_code=subcat["subcategory_code"])

        button_text = f"{subcat['subcategory_name']} ({number_of_items} dona)"

        callback_data = make_cd(level=CURRENT_LEVEL + 1, category=category,
                                subcategory=subcat['subcategory_code'])
        markup.insert(InlineKeyboardButton(text=button_text, callback_data=callback_data))

    # Ortga qaytish tugmasi
    markup.row(InlineKeyboardButton(text="⬅️Ortga", callback_data=make_cd(level=CURRENT_LEVEL - 1)))
    return markup


async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2

    markup = InlineKeyboardMarkup(row_width=1)

    items = await db.get_products(category, subcategory)

    for item in items:
        button_text = f"{item['productname']} ${item['price']}"

        callback_data = make_cd(level=CURRENT_LEVEL + 1, category=category,
                                subcategory=subcategory, item_id=item["id"])
        logging.info(callback_data)
        markup.insert(InlineKeyboardButton(text=button_text, callback_data=callback_data))

    markup.row(InlineKeyboardButton(text="⬅️Ortga", callback_data=make_cd(level=CURRENT_LEVEL - 1,
                                                                          category=category)))
    return markup


def item_keyboard(category, subcateogry, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)

    markup.row(InlineKeyboardButton(text="🛒Xarid qilish",
                                    callback_data=buy_item.new(item_id=item_id)))
    markup.row(InlineKeyboardButton(text="⬅️Ortga",
                                    callback_data=make_cd(level=CURRENT_LEVEL - 1,
                                                          category=category,
                                                          subcategory=subcateogry)))
    return markup
