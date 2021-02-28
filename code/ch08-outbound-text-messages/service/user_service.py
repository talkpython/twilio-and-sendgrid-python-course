from sqlalchemy import or_

from db.order import Order
from db.session import SessionContext
from db.user import User
from models.cake import Cake
from models.customer import Customer


def record_order(u: Customer, c: Cake, price: float):
    with SessionContext(commit_on_success=True) as ctx:

        user = ctx.session.query(User).filter(
            or_(User.email == u.email, User.phone == u.number)
        ).first()

        if not user:
            user = User(name=u.name, phone=u.number, email=u.email)
            ctx.session.add(user)

        order = Order(size=c.size, flavour=c.flavour, topping=c.topping,
                      frosting=c.frosting, price=price)

        user.orders.append(order)

    return order
