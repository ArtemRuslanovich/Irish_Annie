from aiogram import Bot
from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from utils.dbconnect import Request
from keyboards.credits import credits_keyboard

from aiogram.types import CallbackQuery, LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton

async def send_invoice(callback: CallbackQuery):
    bot = callback.bot
    chat_id = callback.message.chat.id

    # Получаем данные из текста кнопки
    credits_amount, price = parse_callback_data(callback.data)

    if credits_amount is None or price is None:
        # Если данные не удалось распарсить, отправляем сообщение об ошибке
        await bot.send_message(chat_id, "Error parsing callback data.")
        return

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
        reply_markup=credits_keyboard
    )

def parse_callback_data(data: str):
    # Парсим данные из строки
    parts = data.split('_')

    if len(parts) < 3:
        # Если не хватает частей, возвращаем None для обозначения ошибки
        return None, None

    credits_amount = int(parts[1])
    price = int(parts[2])
    return credits_amount, price

def calculate_price(credits_amount: int) -> int:
    prices = {
        100: 149,
        250: 299,
        500: 499,
        1000: 899,
        2500: 1799,
        5000: 2999,
        10000: 4999
    }
    return prices.get(credits_amount, 0)

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    bot = pre_checkout_query.bot  # Получаем объект бота из PreCheckoutQuery
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message, request: Request):
    total_amount = message.successful_payment.total_amount
    credits = calculate_credits(total_amount)

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

def calculate_credits(total_amount: int) -> int:
    prices = {
        149: 100,
        299: 250,
        499: 500,
        899: 1000,
        1799: 2500,
        2999: 5000,
        4999: 10000
    }
    return prices.get(total_amount, 0)