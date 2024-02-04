from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

subs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Basic →  $9.99 (18% Discount)',
            callback_data='credits_2000'
        )
    ],
    [
        InlineKeyboardButton(
            text='Pro →  $19.99 (33% Discount)',
            callback_data='credits_5000'
        )
    ],
    [
        InlineKeyboardButton(
            text='Platinum →  $49.99 (50% Discount)',
            callback_data='credits_20000'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])