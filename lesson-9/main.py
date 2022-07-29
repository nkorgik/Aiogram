from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from projects.config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url="https://www.youtube.com/channel/UCOWaWydDLr2unk_F0LcvT1w/videos")
ib2 = InlineKeyboardButton(text='Button 2',
                           url="https://www.youtube.com/channel/UCOWaWydDLr2unk_F0LcvT1w/videos")

ikb.add(ib1, ib2)

@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello World!',
                           reply_markup=ikb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
