import json

import flask
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from models.order import CakeOrder
from models.order_response import OrderResponseModel
from service import user_service

blueprint = flask.Blueprint('order_api', 'order_api')


@blueprint.route('/api/order', methods=['POST'])
def order():
    try:
        data = flask.request.get_json(force=True)
        cake_order = CakeOrder(**data)

        # Create or update user & record order
        db_order = user_service.record_order(
            cake_order.customer,
            cake_order.cake,
            cake_order.price)

        # TODO: Send email receipt + invoice

        # Return order details to user via Studio
        resp = OrderResponseModel(
            order_id=db_order.id, order_date=db_order.created_date,
            email=cake_order.customer.email, price=db_order.price,
            cake=cake_order.cake
        )

        return resp.dict()

    except ValidationError as ve:
        error_body = {"error": str(ve).replace("\n", " ")}
        error_code = 422
    except SQLAlchemyError as se:
        error_body = {"error": str(se).replace("\n", " ")}
        error_code = 500
    except Exception as x:
        error_body = {"error": str(x).replace("\n", " ")}
        error_code = 500

    return flask.Response(json.dumps(error_body),
                          status=error_code,
                          mimetype='application/json')
