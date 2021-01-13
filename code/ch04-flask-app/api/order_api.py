import flask

from models.order import CakeOrder

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order', methods=['POST'])
def order():
    data = flask.request.get_json(force=True)
    cake_order = CakeOrder(**data)

    return {"received": cake_order.dict()}
