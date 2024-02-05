from aiogram.types import Message, CallbackQuery
from aiogram import Bot

STRIPE_PAYMENT_LINK = '*'


async def process_subscribe_platinum(callback_query: CallbackQuery, message: Message):
    # Send a message with the Stripe Payment Link
    await callback_query.message.edit_text(f"You can subscribe by following this link: {STRIPE_PAYMENT_LINK}")