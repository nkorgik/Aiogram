from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
b3 = KeyboardButton(text='Random photo')

kb.add(b1, b2).add(b3)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Рандом')
bp2 = KeyboardButton(text='Главное меню')

kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️',
                           callback_data='like')
ib2 = InlineKeyboardButton(text='👎',
                           callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующая фотка',
                           callback_data='next')

ikb.add(ib1, ib2).add(ib3)
