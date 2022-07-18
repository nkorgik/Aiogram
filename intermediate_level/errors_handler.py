import asyncio

from aiogram import executor, Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked

from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer('sdhfkjsdf')


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update: types.Update, exception: BotBlocked) -> bool:
    print('Низя отправить сообщение, потому что нас заблокировали!')

    return True


if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True)
