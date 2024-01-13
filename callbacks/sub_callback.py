from aiogram import Bot
from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from utils.dbconnect import Request
from keyboards.sub import subscription_keyboard

from aiogram.types import CallbackQuery, LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton


async def subs(callback: CallbackQuery):
    await callback.message.edit_text(
        f"💳 More credits, more fun with Joi. Choose now. 👄👅",
        reply_markup=subscription_keyboard
    )


subscription_prices = {
    'basic': 999,  # 9.99 USD
    'pro': 1999,    # 19.99 USD
    'platinum': 4999  # 49.99 USD
}

async def process_subscription_button(callback_query: CallbackQuery, bot: Bot):
    user_id = callback_query.from_user.id
    subscription_type = callback_query.data.replace('subscribe_', '')  # Получаем тип подписки

    # Получаем цену из словаря
    subscription_price = subscription_prices.get(subscription_type)

    if subscription_price is None:
        await bot.send_message(user_id, "Invalid subscription type.")
        return

    # Здесь вы можете выполнить дополнительные шаги, такие как отправка инвойса или обработка оплаты
    # В зависимости от вашей логики, вам, возможно, потребуется взаимодействовать с API платежного провайдера

    # Пример: отправка сообщения о подтверждении и предложение оплаты
    await bot.send_message(user_id, f"You've selected a {subscription_type} subscription. Please proceed with the payment.")

    # Пример: отправка инвойса (вам потребуется адаптировать этот код под ваш платежный провайдер)
    await bot.send_invoice(
        chat_id=user_id,
        title=f'{subscription_type} subscription',
        description=f'Description of the {subscription_type} subscription.',
        payload=f'Subscription_{subscription_type}',  # Полезная нагрузка, которая может быть использована для идентификации подписки
        provider_token='1877036958:TEST:c5be40a8cc6d3aa94806faad49f6fc9b3d629c2c',
        currency='usd',
        prices=[
            LabeledPrice(
                label=f'{subscription_type} subscription',
                amount=subscription_price
            )
        ],
        start_parameter='subscription',
        provider_data=None,
        need_email=False,
        need_name=False,
        need_phone_number=False,
        protect_content=False,
        request_timeout=15,
        reply_markup=None  # Ваша кастомная клавиатура для инвойса, если нужно
    )