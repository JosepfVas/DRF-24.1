import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


# def convert_rub_to_dollars(amount):
#     """ Конвертирует Рубли в Доллары. """
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(amount * rate)

def create_stripe_product(name, description):
    return stripe.Product.create(name=name, description=description)


def create_stripe_price(amount):
    """ Создает цену в срайпе. """
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "Gold Plan"},
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
