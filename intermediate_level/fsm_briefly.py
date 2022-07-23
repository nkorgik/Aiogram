"""examples
program model
finite-state-machine
"""
from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN_API

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage)


class ProfileStatesGroup(StatesGroup):

    photo = State()
    name = State()
    age = State()
    description = State()


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))

    return kb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Welcome! So as to create profile - type /create',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.reply("Let's create your profile! To begin with, send me your photo!")
    await ProfileStatesGroup.photo.set()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)


