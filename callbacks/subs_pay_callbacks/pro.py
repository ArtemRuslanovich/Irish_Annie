from aiogram.types import Message
from aiogram import Bot

STRIPE_PAYMENT_LINK = '*'


async def process_subscribe_pro(bot: Bot, message: Message):
    # Send a message with the Stripe Payment Link
    await bot.send_message(chat_id=message.chat.id, text=f"You can subscribe by following this link: {STRIPE_PAYMENT_LINK}")