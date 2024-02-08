from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery


user_id = CallbackQuery.from_user.id
credits_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='100 →  $1.49',
            callback_data='credits_100'
        )
    ],
    [
        InlineKeyboardButton(
            text='200 →  $2.99',
            callback_data='credits_200'
        )
    ],
    [
        InlineKeyboardButton(
            text='500 →  $4.99',
            callback_data='credits_500'
        )
    ],
    [
        InlineKeyboardButton(
            text='1000 →  $8.99',
            callback_data='credits_1000'
        )
    ],
    [
        InlineKeyboardButton(
            text='2500 →  $17.99',
            callback_data='credits_2500'
        )
    ],
    [
        InlineKeyboardButton(
            text='5000 →  $29.99',
            callback_data='credits_5000'
        )
    ],
    [
        InlineKeyboardButton(
            text='10000 →  $49.99',
            callback_data='credits_10000'
        )
    ],
    [
        InlineKeyboardButton(
            text=f'❤️Subscribe monthly for 50% discount and 20000 credits❤️',
            url=f'https://probably-kit.github.io/subscription-choice-menu/?user_id={user_id}'
        )
    ],
    [
        InlineKeyboardButton(
            text='◀️ Back',
            callback_data='profile'
        )
    ]
])