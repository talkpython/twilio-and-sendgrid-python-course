import datetime
from typing import List
import sqlalchemy as sa
from sqlalchemy import orm

from db.base_class import SqlAlchemyBase
from db.order import Order


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        index=True)

    name: str = sa.Column(sa.String)
    phone: str = sa.Column(sa.String, index=True)
    email: str = sa.Column(sa.String, index=True)

    orders: List[Order] = orm.relationship("Order", back_populates="user")
