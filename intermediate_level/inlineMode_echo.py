import hashlib

from aiogram import executor, Bot, Dispatcher, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from aiogram.types import InlineQueryResultArticle, InputTextMessageContent  # INLINE MODE!

from config import TOKEN_API

cb = CallbackData('ikb', 'action')  # pattern
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button_1', callback_data=cb.new('push_1'))],  # callback_data = {'action': 'push_1'}
        [InlineKeyboardButton('Button_2', callback_data=cb.new('push_2'))]   # callback_data = {'action': 'push_2'}
    ])

    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text='Welcome to my Aiogram YouTube Bot! Don\'t forget to subscribe to my channel!',
                         reply_markup=get_ikb())


@dp.callback_query_handler(cb.filter(action='push_1'))  # single responsibility principle
async def push_first_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.answer('Hello!')


@dp.callback_query_handler(cb.filter(action='push_2'))
async def push_second_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.answer('World!')


# inlineQuery handlers

@dp.inline_handler()  # process InlineQuery() is formed by Telegram API
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'  # получили текст от пользователя, либо "Echo"
    input_content = InputTextMessageContent(text)  # формируем контент ответного сообщения
    result_id: str = hashlib.md5(text.encode()).hexdigest()  # сделали уникальный ID результата

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Inline Echo Mode 🤕',
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,  #
                                  results=[item],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)



