from pathlib import Path
from typing import Optional

import html2text
import jinja2
import python_http_client
import sendgrid

from db.order import Order
from infrastructure import app_secrets


def send_cake_order_receipt(order: Order):
    client = sendgrid.SendGridAPIClient(app_secrets.sendgrid_api_key)

    from_email = sendgrid.From('michael@talkpython.fm', "Michael Kennedy")
    to_email = sendgrid.To(order.user.email, order.user.name)
    subject = sendgrid.Subject("Your order receipt from Cloud City Cakes")

    html = build_html('email/receipt.html', {'order': order})
    text = html2text.html2text(html)

    # TODO: Build PDF invoice
    # TODO: Attach the invoice to the email

    # Send the email
    message = sendgrid.Mail(from_email, to_email, subject, text, html)
    response: python_http_client.client.Response = client.send(message)

    if response.status_code not in {200, 201, 202}:
        raise Exception(f"Error sending email: {response.status_code}")

    print(f"Sent email successfully: Order {order.id} to {order.user.name} at {order.user.email}")


def build_html(template_file: str, data: dict) -> str:
    template_folder = str(Path(__file__).parent.parent / "templates")
    loader = jinja2.FileSystemLoader(template_folder)
    env = jinja2.Environment(loader=loader)

    template: jinja2.Template = loader.load(env, template_file, None)
    html = template.render(**data)

    return html
