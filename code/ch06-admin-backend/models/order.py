from pydantic import BaseModel

from models.cake import Cake
from models.customer import Customer


class CakeOrder(BaseModel):
    customer: Customer
    cake: Cake
    price: float

    class Config:
        anystr_strip_whitespace = True
