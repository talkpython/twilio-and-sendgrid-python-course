from pydantic import BaseModel


class Customer(BaseModel):
    number: str
    name: str
    email: str

    class Config:
        anystr_strip_whitespace = True
