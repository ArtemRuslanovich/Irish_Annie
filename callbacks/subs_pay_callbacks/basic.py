from aiogram.types import Message

STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/5kA8yL9NC4US4UM144'


async def process_subscribe_basic(message: Message):
    # Send a message with the Stripe Payment Link
    await message.answer("You can subscribe by following this link: " + STRIPE_PAYMENT_LINK)