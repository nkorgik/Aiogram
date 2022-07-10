from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True) # default - False
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
kb.add(b1).insert(b2).add(b3)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш Бот!",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Наш бот умеет отправлять фотографии",
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHfQfXQD-FhEfRlBCrWZiLi5PMIYWLRr2d6A&usqp=CAU')
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
