from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

feedback_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='👍 Like',
            callback_data='like'
        ),
        InlineKeyboardButton(
            text='👎 Dislike',
            callback_data='dislike'
        )
    ]
])