from pydantic import BaseModel


class Cake(BaseModel):
    topping: str
    frosting: str
    flavour: str
    size: str

    class Config:
        anystr_strip_whitespace = True
