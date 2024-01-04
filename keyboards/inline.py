from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ...

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Settings',
            callback_data='settings'
        )
    ],
    [
        InlineKeyboardButton(
            text='Info',
            callback_data='info'
        ),
        InlineKeyboardButton(
            text='Profile',
            callback_data='profile'
        )
    ]
])

settings_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='About you',
            callback_data='customer'
        ),
        InlineKeyboardButton(
            text='About Alise',
            callback_data='bot_settings'
        )
    ],
    [
        InlineKeyboardButton(
            text='Back',
            callback_data='back_start'
        )
    ]
])

info_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Back',
            callback_data='back_start'
        )
    ]
])

profile_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Credits',
            callback_data='show_credits'
        )
    ],
    [
        InlineKeyboardButton(
            text='Back',
            callback_data='back_start'
        )
    ]
])

customer_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Your name',
            callback_data='set_name'
        ),
        InlineKeyboardButton(
            text='your gender',
            callback_data='set gender'
        )
    ],
    [
        InlineKeyboardButton(
            text='Back',
            callback_data='back_settings'
        )
    ]
])

bot_settings_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Bot character',
            callback_data='set_character'
        ),
        InlineKeyboardButton(
            text='Bot style',
            callback_data='set_style'
        )
    ],
    [
        InlineKeyboardButton(
            text='Back',
            callback_data='back_settings'
        )
    ]
])