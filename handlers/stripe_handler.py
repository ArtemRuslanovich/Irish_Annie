import stripe
from aiohttp import web
import os
import json
from utils.dbconnect import Request

# Установите ваш Stripe секретный ключ здесь
stripe.api_key = os.getenv('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')

credits_mapping = {
    'price_basic': 2000,  # ID цены для базовой подписки
    'price_pro': 5000,    # ID цены для профессиональной подписки
    'price_platinum': 20000,  # ID цены для платиновой подписки
}

async def create_checkout_session(request):
    data = await request.json()
    user_id = data['user_id']  # Получение user_id из запроса
    price_id = data['price_id']  # Получение price_id подписки

    # Определение количества кредитов на основе price_id
    credits = credits_mapping.get(price_id, 0)  # Возвращает 0, если price_id нет в словаре

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://vast-ridge-79175-71505a819c13.herokuapp.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://vast-ridge-79175-71505a819c13.herokuapp.com/cancel',
            metadata={'user_id': user_id, 'credits': credits}  # Добавление user_id и credits в метаданные
        )
        return web.json_response({
            'id': session.id
        })
    except Exception as e:
        return web.Response(text=str(e), status=500)
    
async def stripe_webhook(request, req: Request):
    payload = await request.text()
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, "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"
        )
    except ValueError as e:
        # Неверный payload
        return web.Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Неверная подпись
        return web.Response(status=400)

    # Обработка события успешной оплаты
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = session['metadata']['user_id']
        credits = session['metadata']['credits']
        await req.add_credits(user_id, credits)

    return web.Response(text=json.dumps({'status': 'success'}), status=200)