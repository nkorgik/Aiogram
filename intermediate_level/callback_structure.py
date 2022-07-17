"""In this lesson we're gonna take a look at callback: types.CallbackQuery structure"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
])

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://assets.traveltriangle.com/blog/wp-content/uploads/2018/03/acj-2003-beautiful-landscapes-around-the-world-23.jpg',
                         caption='Нравится ли тебе фотография?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    print(callback)
    if callback.data == 'like':
        await callback.answer('Тебе понравилась фотография!')
    await callback.answer('Тебе не понравилось!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
