from aiogram import types

products = [
    {
        "id": "001",
        "title": "01 Burger",
        "url": "https://images.unsplash.com/photo-1530554764233-e79e16c91d08?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
        "description": "Andijon tezkor mazali burgeri, Narxi 8900sum"
    },
{
        "id": "002",
        "title": "02 Hotdog",
        "url": "https://images.unsplash.com/photo-1530554764233-e79e16c91d08?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
        "description": "Andijon tezkor mazali hotdog, Narxi 6900sum"
    },
{
        "id": "003",
        "title": "03 Lavash",
        "url": "https://images.unsplash.com/photo-1530554764233-e79e16c91d08?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
        "description": "Andijon tezkor mazali lavash, Narxi 5900sum"
    },
]

inline_query_product = []
for product in products:
    inline_query_product.append(
        types.InlineQueryResultArticle(
            id=product["id"],
            title=product["title"],
            input_message_content=types.InputTextMessageContent(
                message_text=f'{product["title"]} ga link: {product["url"]}'
            ),
            url=product['url'],
            description=product["description"]
        )
    )




