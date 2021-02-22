from typing import List

from sqlalchemy.orm import subqueryload

from db.order import Order
from db.session import SessionContext


def all_cake_orders() -> List[Order]:
    with SessionContext(commit_on_success=True) as ctx:

        orders = ctx.session.query(Order)\
            .options(subqueryload(Order.user)) \
            .order_by(Order.created_date.desc())\
            .all()

    return orders
