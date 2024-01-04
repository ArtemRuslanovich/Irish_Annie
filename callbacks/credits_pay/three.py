from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from aiogram import Router, F, Bot, Dispatcher
from utils.dbconnect import Request

async def three_credits(callback: CallbackQuery, bot : Bot):
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title='3000 credits',
        description='3000 credits wiil be avalible in yout account',
        payload='Payment through a bot',
        provider_token='1877036958:TEST:c5be40a8cc6d3aa94806faad49f6fc9b3d629c2c',
        currency='usd',
        prices=[
            LabeledPrice(
                label = '3000 credits',
                amount=2199
            )
        ],
        start_parameter='Net',
        provider_data=None,
        need_email=False,
        need_name=False,
        need_phone_number=False,
        protect_content=False,
        request_timeout=15
    )
