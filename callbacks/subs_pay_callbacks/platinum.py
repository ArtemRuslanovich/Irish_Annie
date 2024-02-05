from aiogram.types import CallbackQuery
from aiogram import Bot

STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/test_123'

async def process_subscribe_platinum(callback_query: CallbackQuery):
    # Attempt to edit the message to include the Stripe Payment Link
    new_text = f"You can subscribe by following this link: {STRIPE_PAYMENT_LINK}"
    
    # Check if the message is already what you're trying to set it to
    if callback_query.message.text != new_text:
        await callback_query.message.edit_text(new_text)
    else:
        # If the message is already displaying the link, consider acknowledging the action without editing
        await callback_query.answer("You're already on the subscription page!", show_alert=True)
