import flask

from service import order_service

blueprint = flask.Blueprint('admin', 'admin')


@blueprint.route('/admin')
def index():
    orders = order_service.all_cake_orders()
    return flask.render_template('admin/index.html', orders=orders)


@blueprint.route('/admin/fulfill/<order_id>')
def fulfill(order_id: int):
    order = order_service.find_order_by_id(order_id)
    if not order:
        return flask.abort(404)

    order_service.fulfill_order(order_id)

    # TODO: Send whatsapp message to notify the customer!

    return flask.redirect('/admin')

