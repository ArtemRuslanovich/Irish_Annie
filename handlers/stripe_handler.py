import stripe
from aiohttp import web
import os
import json
from utils.dbconnect import Request

# Установите ваш Stripe секретный ключ здесь
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

async def create_checkout_session(request):
    data = await request.json()
    user_id = data['user_id']  # Получение user_id из запроса
    price_id = data['price_id']  # Получение price_id подписки

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://example.com/cancel',
            metadata={'user_id': user_id}
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
            payload, sig_header, "whsec_..."
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