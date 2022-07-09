from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN_API

import string
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer('Данный бот умеет отправлять рандомные символы латинского алфавита')
    await message.delete()

@dp.message_handler(commands=['count'])
async def check_count(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.reply('YES')
    await message.reply('NO')

@dp.message_handler() #ASCII
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(dp)
