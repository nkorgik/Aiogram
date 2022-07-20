import hashlib

from aiogram import executor, Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent  # INLINE MODE!

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

user_data = ''

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Введите число!')


@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.reply('Ваши данные сохранены!')


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode='html')

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo Bot!',
        description='Привет, я не простой ЭХО БОТ!',
    )

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)



