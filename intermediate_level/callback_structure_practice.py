"""In this lesson we're gonna take a look at callback: types.CallbackQuery structure on practice"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Like', callback_data='like'), InlineKeyboardButton('Dislike', callback_data='dislike')],
    [InlineKeyboardButton('Close keyboard', callback_data='close')]
])


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.usnews.com/object/image/00000162-f3a3-d0d5-a57f-fbf32fe60000/1-intro-iguazu-falls.jpg?update-time=1524505980902&size=responsive640',
                         caption='Do you like?',
                         reply_markup=ikb)


@dp.callback_query_handler(text='close')
async def ikb_close_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler()
async def ikb_close_cb_handler(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        if callback.data == 'like':
            await callback.answer(show_alert=False,
                                  text='Тебе понравилось')
            is_voted = True  # client has voted
        await callback.answer(show_alert=False,
                              text='Тебе не понравилось понравилось')
        is_voted = True
    await callback.answer('Ты уже голосовал',
                          show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
