from pydantic import BaseModel # type: ignore[reportMissingImports]
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id:int
    name:str
    address: Address # refrence to Address model

address = Address(
    street="123 Main St",
    city="New York",
    postal_code="10001"
)

user = User(
    id=1,
    name="John Doe",
    address=address
)

user_data = {
    "id": 2,
    "name": "kushagra",
    "address": {
        "street": "456 Elm St",
        "city": "Los Angeles",
        "postal_code": "90001"
    }
}

printed_user = User(**user_data) # **astric used for spreading the dictionary into keyword arguments for the User model
print("User data with nested Address model:", printed_user)