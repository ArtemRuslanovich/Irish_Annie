from aiogram import Bot
from utils.dbconnect import Request
from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery

async def send_invoice(callback: CallbackQuery):
    bot = callback.bot
    chat_id = callback.message.chat.id

    credits_amount = callback.data.replace('credits_', '')

    if credits_amount is None:
        await bot.send_message(chat_id, "Error parsing callback data.")
        return

    # Преобразуем credits_amount в int
    credits_amount = int(credits_amount)

    # Получаем цену с использованием функции calculate_price
    price = calculate_price(credits_amount)

    await bot.send_invoice(
        chat_id=chat_id,
        title=f'{credits_amount} credits',
        description=f'{credits_amount} credits will be available in your account',
        payload='Payment through a bot',
        provider_token='1877036958:TEST:c5be40a8cc6d3aa94806faad49f6fc9b3d629c2c',
        currency='usd',
        prices=[
            LabeledPrice(
                label=f'{credits_amount} credits',
                amount=price
            )
        ],
        start_parameter='Net',
        provider_data=None,
        need_email=False,
        need_name=False,
        need_phone_number=False,
        protect_content=False,
        request_timeout=15,
        reply_markup=None
    )

def calculate_price(credits_amount: int) -> int:
    prices = {
        100: 149,
        200: 299,
        500: 499,
        1000: 899,
        2500: 1799,
        5000: 2999,
        10000: 4999
    }
    return prices.get(credits_amount, 0)

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    bot = pre_checkout_query.bot
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message, request: Request):
    total_amount = message.successful_payment.total_amount
    credits = calculate_credits(total_amount)

    user_id = message.from_user.id
    await request.add_credits(user_id, credits)

    msg = """Thank You for loving me 💋 Back to our conversation...\nNow where were we? Let's keep chatting..."""
    await message.answer(msg)

def calculate_credits(total_amount: int) -> int:
    prices = {
        149: 100,
        299: 200,
        499: 500,
        899: 1000,
        1799: 2500,
        2999: 5000,
        4999: 10000
    }
    return prices.get(total_amount, 0)