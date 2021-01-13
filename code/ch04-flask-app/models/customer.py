from pydantic import BaseModel


class Customer(BaseModel):
    number: str
    name: str
    email: str
