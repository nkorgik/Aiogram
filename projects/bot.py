# list of all products

from aiogram import types, executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import TOKEN_API
from keyboards import *
import sqlite_db

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot,
                storage=storage)


class ProductStatesGroup(StatesGroup):

    title = State()
    photo = State()

    new_title = State()


async def on_startup(_):
    await sqlite_db.db_connect()
    print('Подключение к БД выполнено успешно')


async def show_all_products(callback: types.CallbackQuery, products: list) -> None:
    for product in products:
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=product[2],
                             caption=f'<b>{product[1]}</b> {product[0]}',
                             parse_mode='HTML',
                             reply_markup=get_edit_ikb(product[0]))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать!',
                           reply_markup=get_start_kb())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.answer('Вы отменили действие!',
                         reply_markup=get_start_kb())


@dp.message_handler(commands=['products'])
async def cmd_products(message: types.Message):
    await message.delete()
    await message.answer('Управление продуктами',
                         reply_markup=get_products_ikb())


@dp.callback_query_handler(text='get_all_products')
async def cb_get_all_products(callback: types.CallbackQuery):
    products = await sqlite_db.get_all_products()  #

    if not products:
        await callback.message.delete()
        await callback.message.answer('Вообще продуктов нет!')
        return await callback.answer()

    await callback.message.delete()
    await show_all_products(callback, products)
    await callback.answer()


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

    await sqlite_db.create_new_product(state)
    await message.reply('Спасибо, ваш продукт создан!',
                        reply_markup=get_start_kb())

    await state.finish()


@dp.callback_query_handler(products_cb.filter(action='delete'))
async def cb_delete_product(callback: types.CallbackQuery, callback_data: dict):
    await sqlite_db.delete_product(callback_data['id'])

    await callback.message.reply('Ваш продукт был успешно удалён!')
    await callback.answer()


@dp.callback_query_handler(products_cb.filter(action='edit'))
async def cb_edit_product(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Отправь нам новое название продукта!',
                                  reply_markup=get_cancel_kb())
    await ProductStatesGroup.new_title.set()

    async with state.proxy() as data:
        data['product_id'] = callback_data['id']

    await callback.answer()


@dp.message_handler(state=ProductStatesGroup.new_title)
async def load_new_title(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        await sqlite_db.edit_product(data['product_id'], message.text)

    await message.reply('Новое название продукта установлено!',
                        reply_markup=get_start_kb())
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
