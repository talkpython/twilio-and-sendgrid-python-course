import flask

from models.order import CakeOrder

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order', methods=['POST'])
def order():
    data = flask.request.get_json(force=True)
    cake_order = CakeOrder(**data)

    # TODO: Create or update user & record order
    # TODO: Send email receipt + invoice
    # TODO: Return order details to user via Studio

    print(cake_order)

    return {"received": cake_order.dict()}
