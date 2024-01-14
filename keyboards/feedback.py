from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

feedback_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='👍',
            callback_data='like'
        ),
        InlineKeyboardButton(
            text='👎',
            callback_data='dislike'
        )
    ]
])