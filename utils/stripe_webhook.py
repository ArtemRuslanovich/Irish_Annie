from flask import Flask, request, jsonify
import stripe
import os

app = Flask(__name__)

# Stripe API secret key
stripe.api_key = os.getenv('whsec_9b51de4c6d1c0be356f807cb2eaf26f0675c1d1169f71dce134d9e06e263820f')

endpoint_secret = 'whsec_9b51de4c6d1c0be356f807cb2eaf26f0675c1d1169f71dce134d9e06e263820f'

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return 'Invalid signature', 400

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Here, implement your logic to handle successful payment
        handle_successful_payment(session)

    return jsonify(success=True), 200

def handle_successful_payment(session):
    # Get the customer's Telegram ID or any other identifier from metadata
    telegram_id = session.get('metadata', {}).get('telegram_id')

    if telegram_id:
        # Perform operations such as confirming the subscription,
        # notifying the user, updating the database, etc.
        print(f"Handled payment for Telegram user {telegram_id}")
        # You would replace the print statement with actual logic.

if __name__ == "__main__":
    app.run(port=4242)