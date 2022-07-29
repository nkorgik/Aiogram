from aiogram import types, executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import TOKEN_API
from keyboards import get_products_ikb, products_cb, get_start_kb, get_cancel_kb
import sqlite_db

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot,
                storage=storage)


class ProductStatesGroup(StatesGroup):

    title = State()
    photo = State()


async def on_startup(_):
    await sqlite_db.db_connect()
    print('Подключение к БД выполнено успешно')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать!',
                           reply_markup=get_start_kb())


@dp.message_handler(commands=['products'])
async def cmd_products(message: types.Message):
    await message.answer('Управление продуктами',
                         reply_markup=get_products_ikb())


@dp.callback_query_handler(text='get_all_products')
async def cb_get_all_products(callback: types.CallbackQuery):
    products = await sqlite_db.get_all_products()

    if not products:
        await callback.message.delete()
        await callback.message.answer('Вообще продуктов нет!')
        return await callback.answer()

    await callback.message.answer(products)


@dp.callback_query_handler(text='add_new_product')
async def cb_add_new_product(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer('Отправь название продукта!',
                                  reply_markup=get_cancel_kb())

    await ProductStatesGroup.title.set()


@dp.message_handler(state=ProductStatesGroup.title)
async def handle_title(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['title'] = message.text

    await message.reply('А теперь нам фотографию!')
    await ProductStatesGroup.next()


@dp.message_handler(lambda message: not message.photo, state=ProductStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('Это не фотография!')


@dp.message_handler(content_types=['photo'], state=ProductStatesGroup.photo)
async def handle_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Спасибо, ваш продукт создан!')

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
