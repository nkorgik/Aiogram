from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

products_cb = CallbackData('product', 'id', 'action')

def get_products_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Просмотр всех продуктов', callback_data='get_all_products')],
        [InlineKeyboardButton('Добавить новый продукт', callback_data='add_new_product')],
    ])

    return ikb


def get_edit_ikb(product_id: int) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Редактировать продукт', callback_data=products_cb.new(product_id, 'edit'))],
        [InlineKeyboardButton('Удалить продукт', callback_data=products_cb.new(product_id, 'delete'))],
    ])

    return ikb


def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/products')]
    ], resize_keyboard=True)

    return kb


def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/cancel')]
    ], resize_keyboard=True)

    return kb
