import flask

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order', methods=['POST'])
def order():
    data = flask.request.get_json(force=True)
    return {"received": data}
