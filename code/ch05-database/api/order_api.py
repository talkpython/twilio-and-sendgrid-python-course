import flask

from models.order import CakeOrder
from service import user_service

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

    # TODO: Send email receipt + invoice

    # TODO: Return order details to user via Studio

    print(cake_order)

    return {"received": cake_order.dict()}
