import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import random


from config import TOKEN_API
from keyboards import kb, kb_photo, ikb


bot = Bot(token=TOKEN_API)  # создаём экземпляр бота, подключаясь к API
dp = Dispatcher(bot=bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>"""

arr_photos = ["https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/08/03/america-the-beautiful-ss/adirondack-park-new-york-state.jpg.rend.hgtvcom.616.462.suffix/1491580836599.jpeg",
              "https://i.ytimg.com/vi/u71QsZvObHs/maxresdefault.jpg",
              "https://images.unsplash.com/photo-1613967193490-1d17b930c1a1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXRpZnVsJTIwbGFuZHNjYXBlfGVufDB8fDB8fA%3D%3D&w=1000&q=80"]

photos = dict(zip(arr_photos, ['Lake', 'Waterfall', 'Shore']))
random_photo = random.choice(list(photos.keys()))

flag = False


async def on_startup(_):
    print('Я запустился!')


async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)


@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомная фотка!',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


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


@dp.message_handler(commands=['location'])
async def cmd_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(0, 50),
                            longitude=random.randint(0, 50))


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo  # ! нежелательно использование глобальных переменных
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer("Вам понравилось!")
            flag = not flag
        else:
            await callback.answer("Вы уже лайкнули!")
        # await callback.message.answer('Вам понравилось!')
    elif callback.data == 'dislike':
        await callback.answer("Вам не понравилось!")
        # await callback.message.answer('Вам не понравилось!')
    elif callback.data == 'main':
        await callback.message.answer(text='Добро пожаловать в главное меню!',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=photos[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
