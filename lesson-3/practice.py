from aiogram import Bot, Dispatcher, types, executor

from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>показывает список команд</em>
<b>/give</b> - <em>отправляет кота</em>
<b>/start</b> - <em>запускает бота</em>"""


async def on_startup(_):
    print('Я запустился')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')

@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAO3YsmWkTZGlI3-C20hAR0Ni7VX1OwAAlgAA845CA0YTGAbMvUI0ykE")

# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=str(message.text.count('✅')))

# @dp.message_handler(commands=['give'])
# async def send_sticker(message: types.Message):
#     await message.answer("Смотри какой котик ❤️")
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAEFO5ViyWw0_ma5hwag-9xvvpO3GZSA6gACWAADzjkIDRhMYBsy9QjTKQQ")
#
# @dp.message_handler()
# async def send_sticker(message: types.Message):
#     if message.text == "❤️":
#         await message.answer("🖤")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
