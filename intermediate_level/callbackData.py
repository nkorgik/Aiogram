from aiogram.utils.callback_data import CallbackData

from aiogram import executor, Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')
cb_2 = CallbackData('ikb_2', 'action')


ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Button', callback_data=cb.new('push')), InlineKeyboardButton('Butn21', callback_data=cb_2.new('push'))]
])


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Text',
                         reply_markup=ikb)


@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('Something!')


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
