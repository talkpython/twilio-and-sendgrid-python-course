import datetime
from typing import List, Optional

from sqlalchemy.orm import subqueryload

from db.order import Order
from db.session import SessionContext


def all_cake_orders() -> List[Order]:
    with SessionContext() as ctx:
        orders = ctx.session.query(Order) \
            .options(subqueryload(Order.user)) \
            .order_by(Order.created_date.desc()) \
            .all()

    return orders


def find_order_by_id(order_id: int) -> Optional[Order]:
    with SessionContext() as ctx:
        order = ctx.session.query(Order) \
            .options(subqueryload(Order.user)) \
            .filter(Order.id == order_id)\
            .first()
        return order


def fulfill_order(order_id: int) -> bool:
    with SessionContext(commit_on_success=True) as ctx:
        order = ctx.session.query(Order).filter(Order.id == order_id).first()
        if not order:
            return False

        if order.fulfilled_date:
            return True

        order.fulfilled_date = datetime.datetime.now()

        # Forgot this in the video version. No harm since we don't use it
        # but might as well make the function consistent, right? :)
        return True  
