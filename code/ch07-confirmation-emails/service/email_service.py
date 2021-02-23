from typing import Optional

import sendgrid

from db.order import Order

key_name: Optional[str] = None
api_key: Optional[str] = None


def send_cake_order_receipt(order: Order):
    client = sendgrid.SendGridAPIClient(api_key)
    # TODO: Gather email details: name, email, and so on.
    # TODO: Build PDF invoice
    # TODO: Generate HTML content
    # TODO: Attach the invoice to the email
    # TODO: Send the email
    print(f"Will send email about {order} to {order.user.name}")
