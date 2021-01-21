import datetime


class Order:
    id: int
    created_date: datetime.datetime
    fulfilled_date: datetime.datetime

    size: str
    flavour: str
    topping: str
    frosting: str
    price: float

    user_id: int
    user: "User"
