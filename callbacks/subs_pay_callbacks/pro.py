from aiogram.types import Message

STRIPE_PAYMENT_LINK = '*'


async def process_subscribe_pro(message: Message):
    # Send a message with the Stripe Payment Link
    await message.answer("You can subscribe by following this link: " + STRIPE_PAYMENT_LINK)