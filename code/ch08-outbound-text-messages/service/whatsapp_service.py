from db.order import Order
from infrastructure import app_secrets
from twilio.rest import Client


def send_cake_ready(order: Order):
    client = Client(username=app_secrets.twilio_sid, password=app_secrets.twilio_key)

