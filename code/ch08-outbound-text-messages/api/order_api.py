import flask

from models.order import CakeOrder
from models.order_response import OrderResponseModel
from service import user_service, email_service

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order', methods=['POST'])
def order():
    data = flask.request.get_json(force=True)
    cake_order = CakeOrder(**data)

    # Create or update user & record order
    db_order = user_service.record_order(
        cake_order.customer,
        cake_order.cake,
        cake_order.price)

    email_service.send_cake_order_receipt(db_order)

    # Return order details to user via Studio
    resp = OrderResponseModel(
        order_id=db_order.id, order_date=db_order.created_date,
        email=cake_order.customer.email, price=db_order.price,
        cake=cake_order.cake
    )

    return resp.dict()
