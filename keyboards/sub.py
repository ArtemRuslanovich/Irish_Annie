from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

subscription_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Basic - 2000 credits - 9.99$ (18% Discount)',
            callback_data='subscribe_basic'
        )
    ],
    [
        InlineKeyboardButton(
            text='Pro - 5000 credits - 19.99$ (33% Discount)',
            callback_data='subscribe_pro'
        )
    ],
    [
        InlineKeyboardButton(
            text='Platinum - 20000 credits - 49.99$ (50% Discount)',
            callback_data='subscribe_platinum'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])
