from aiogram import Bot, Dispatcher, executor, types


# бот - сервер, который будет взаимодействовать с API Telegram.
TOKEN_API = "5554845070:AAEaNyyWnTNuFRsGgnBBpuKysL9gi9txA6Q" # авторизационный токен для подключения к телеграм API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # написать сообщение text


if __name__ == '__main__':
    executor.start_polling(dp)
