import flask

from service import order_service

blueprint = flask.Blueprint('admin', 'admin')


@blueprint.route('/admin')
def index():
    orders = order_service.all_cake_orders()
    return flask.render_template('admin/index.html', orders=orders)
