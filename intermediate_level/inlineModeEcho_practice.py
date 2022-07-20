import hashlib

from aiogram import executor, Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent  # INLINE MODE!

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


# inlineQuery handlers


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    if text == 'photo':
        input_content = InputTextMessageContent('This is a photo')
    else:
        input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(
        id=result_id,
        input_message_content=input_content,
        title=text,
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item])


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)



