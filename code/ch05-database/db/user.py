import datetime
from typing import List
from db.order import Order


class User:
    id: int
    created_date: datetime.datetime

    name: str
    phone: str
    email: str

    orders: List[Order]
