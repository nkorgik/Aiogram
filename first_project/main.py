from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random

from config import TOKEN_API
from keyboards import kb, kb_photo


bot = Bot(token=TOKEN_API)  # создаём экземпляр бота, подключаясь к API
dp = Dispatcher(bot=bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>"""

arr_photos = ["https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/08/03/america-the-beautiful-ss/adirondack-park-new-york-state.jpg.rend.hgtvcom.616.462.suffix/1491580836599.jpeg",
              "https://i.ytimg.com/vi/u71QsZvObHs/maxresdefault.jpg",
              "https://images.unsplash.com/photo-1613967193490-1d17b930c1a1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXRpZnVsJTIwbGFuZHNjYXBlfGVufDB8fDB8fA%3D%3D&w=1000&q=80"]

async def on_startup(_):
    print('Я запустился!')


@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Чтобы отправить рандомную фотографию - нажми на кнопку "Рандом"',
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals="Рандом"))
async def send_random_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(arr_photos))


@dp.message_handler(Text(equals="Главное меню"))
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню!',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Добро пожаловать в наш бот! 🐝',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_help(message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgQAAxkBAAEFSnRi0oSKdBsMkJrWq1Wb_gJe4bH8lgACzAADzjkIDd9nfGV-RLlkKQQ")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
