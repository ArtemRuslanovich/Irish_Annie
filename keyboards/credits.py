from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

credits_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='1000 →  7.99$',
            callback_data='1000'
        )
    ],
    [
        InlineKeyboardButton(
            text='2000 →  14.99$',
            callback_data='2000'
        )
    ],
    [
        InlineKeyboardButton(
            text='3000 →  20.99$',
            callback_data='3000'
        )
    ],
    [
        InlineKeyboardButton(
            text='4000 →  25.99$',
            callback_data='4000'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])