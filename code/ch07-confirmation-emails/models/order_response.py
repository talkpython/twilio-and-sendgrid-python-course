import datetime

from pydantic import BaseModel

from models.cake import Cake


class OrderResponseModel(BaseModel):
    order_id: int
    order_date: datetime.datetime
    email: str
    price: float
    cake: Cake
