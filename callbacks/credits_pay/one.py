from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from aiogram import Router, F, Bot, Dispatcher
from utils.dbconnect import Request
from aiogram.types import ContentType
from aiogram import Router


async def one_credits(callback: CallbackQuery, bot : Bot):
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title='1000 credits',
        description='1000 credits wiil be avalible in yout account',
        payload='Payment through a bot',
        provider_token='1877036958:TEST:c5be40a8cc6d3aa94806faad49f6fc9b3d629c2c',
        currency='usd',
        prices=[
            LabeledPrice(
                label = '1000 credits',
                amount=799
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

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message, request: Request):
    # Получаем сумму платежа в центах
    total_amount = message.successful_payment.total_amount

    # Определение количества кредитов в зависимости от суммы платежа
    if total_amount == 799:  # 7.99$
        credits = 1000
    elif total_amount == 1499:  # 14.99$
        credits = 2000
    elif total_amount == 2199:  # 21.99$
        credits = 3000
    elif total_amount == 2599:  # 25.99$
        credits = 4000
    else:
        # Если сумма не совпадает с ожидаемыми значениями, установите значение по умолчанию
        credits = 0

    user_id = message.from_user.id
    await request.add_credits(user_id, credits)

    msg = """
🌟 **Thank you for your magical payment!**

Hello enchanting soul! 🌈 Your payment has just sprinkled a dash of stardust into our universe. 🚀

*Your generosity sparkles like the stars!* Your support means the world to us, and we're floating on air knowing you've chosen to join our journey.

✨ *May your days be filled with joy and wonder!* If you ever need a sprinkle of magic or have questions, we're here for you.

Sending you beams of gratitude and a universe of thanks! 🌌💖

With love and cosmic energy,
Alisa
"""
    await message.answer(msg)
