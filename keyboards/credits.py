from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

credits_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='100 →  1.49$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='200 →  2.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='500 →  4.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='1000 →  8.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='2500 →  17.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='5000 →  29.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='10000 →  49.99$',
            callback_data='credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])