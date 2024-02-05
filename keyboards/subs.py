from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

subs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Basic →  $9.99 (18% Discount)',
            callback_data='sabs'
        )
    ],
    [
        InlineKeyboardButton(
            text='Pro →  $19.99 (33% Discount)',
            callback_data='sobs'
        )
    ],
    [
        InlineKeyboardButton(
            text='Platinum →  $49.99 (50% Discount)',
            callback_data='sibs'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])