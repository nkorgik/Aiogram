import uuid

from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_link(inline_query: types.InlineQuery) -> None:
    result_id: str = str(uuid.uuid4())

    item = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent('<i>Take your link!</i>',
                                                      parse_mode='html'),
        title='YouTube',
        description='That\'s my YouTube channel!',
        url='https://www.youtube.com/channel/UCOWaWydDLr2unk_F0LcvT1w/videos',
        hide_url=False,
        thumb_url='https://www.youtube.com/img/desktop/yt_1200.png',
        id=result_id,
    )

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
