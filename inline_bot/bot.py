from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Кнопка 1', callback_data='menu_1'),
         InlineKeyboardButton('Кнопка 2', callback_data='menu_2'),
         InlineKeyboardButton('Кнопка 3', callback_data='menu_3'),
         InlineKeyboardButton('Кнопка 4', callback_data='menu_4'), ]
    ])

    return ikb


def get_back_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Назад', callback_data='menu_back')]
    ])

    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Какой-то текст - описание',
                           reply_markup=get_ikb())


@dp.callback_query_handler(text='menu_1')
async def cb_menu_1(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Ты нажал на кнопку 1',
                                     reply_markup=get_back_ikb())


@dp.callback_query_handler(text='menu_2')
async def cb_menu_1(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Ты нажал на кнопку 2',
                                     reply_markup=get_back_ikb())


@dp.callback_query_handler(text='menu_3')
async def cb_menu_1(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Ты нажал на кнопку 3',
                                     reply_markup=get_back_ikb())


@dp.callback_query_handler(text='menu_4')
async def cb_menu_1(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Ты нажал на кнопку 4',
                                     reply_markup=get_back_ikb())


@dp.callback_query_handler(text='menu_back')
async def cb_menu_back(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text='Какой-то текст - описание',
                                     reply_markup=get_ikb())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)