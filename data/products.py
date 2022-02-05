from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product

ds_praktikum = Product(
    title="Data Science suniy intelleknt",
    description="Kursga tolov uchun quyidagi tugmani bosing",
    currency="USD",
    prices=[LabeledPrice(
        label="Praktikum",
        amount=15000),
        LabeledPrice(
            label="chegirma",
            amount=-1000,
        )
    ],
    start_parameter="create_inv_ds_praktikum",
    need_email=False,
    need_name=True,
    need_phone_number=True,
    photo_url='https://images.unsplash.com/photo-1538439907460-1596cafd4eff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2912&q=80',
    photo_width=851,
    photo_height=1280,
)

python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=500,  # 5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,  # 1.00$
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://i.imgur.com/0IvPPun.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,  # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Fargo (3 kun)",
    prices=[LabeledPrice(
        "Maxsus quti", 100
    ),
        LabeledPrice(
            "3 ish kunida yetkashiz", 100
        )
    ]
)

FAST_SHIPPING = types.ShippingOption(
    id="post_fast",
    title="EXpress pochta 1 kun",
    prices=[LabeledPrice(
        "1 kunda yetkazish", 100
    )]
)

PICKUP_SHIPPING = types.ShippingOption(
    id="pickup",
    title="Do'kondan olib ketihs",
    prices=[LabeledPrice("Yetkazib berishsiz", -100)]
)
