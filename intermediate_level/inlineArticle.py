import uuid

from aiogram import types, executor, Bot, Dispatcher

from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_article(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Empty'
    input_content_bold = types.InputTextMessageContent(message_text=f'*{text}*',
                                                       parse_mode='markdown')
    input_content_italic = types.InputTextMessageContent(message_text=f'_{text}_',
                                                         parse_mode='markdown')

    item_1 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_bold,
        title='Bold',
        description=text,
        thumb_url='https://static.tildacdn.com/tild3431-3464-4164-b838-343934373537/Bold_logo.jpg',
    )

    item_2 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_italic,
        title='Italic',
        description=text,
        thumb_url='https://cdn.shopify.com/s/files/1/2791/8222/files/italiclogo400x100_410x2_a55cbb9e-32f6-42ba-a6c8-06e62883ccf0.png?height=628&pad_color=fff&v=1551276189&width=1200',
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_1, item_2],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)