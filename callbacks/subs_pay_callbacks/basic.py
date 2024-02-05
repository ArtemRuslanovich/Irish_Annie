from aiogram.types import Message, CallbackQuery
from aiogram import Bot

STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/5kA8yL9NC4US4UM144'


async def process_subscribe_basic(callback_query: CallbackQuery, message: Message):
    # Send a message with the Stripe Payment Link
    await callback_query.message.edit_text(f"You can subscribe by following this link: {STRIPE_PAYMENT_LINK}")