from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="YouTube",
                           url="https://www.youtube.com/channel/UCOWaWydDLr2unk_F0LcvT1w/videos")
ib2 = InlineKeyboardButton(text="Google",
                           url="https://www.google.com")
ikb.add(ib1).add(ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b = KeyboardButton(text="/links")
kb.add(b)
