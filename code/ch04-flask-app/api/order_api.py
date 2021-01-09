import flask

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order')
def order():
    return {"ordered": True}
