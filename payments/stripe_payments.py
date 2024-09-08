import stripe
from flask import jsonify
from config import Config

stripe.api_key = Config.STRIPE_API_KEY

def create_checkout_session():
    """Создает Stripe Checkout сессию для оплаты."""
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Image Processing Subscription',
                    },
                    'unit_amount': 1000,  # Цена в центах
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://yourdomain.com/success',
            cancel_url='https://yourdomain.com/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403
