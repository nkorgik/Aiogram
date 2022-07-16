from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API
from keyboards import kb


bot = Bot(token=TOKEN_API)  # создаём экземпляр бота, подключаясь к API
dp = Dispatcher(bot=bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>"""


async def on_startup(_):
    print('Я запустился!')


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
