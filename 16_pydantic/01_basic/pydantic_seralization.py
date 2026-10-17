'''
Serialization in Pydantic :-

take pydantic models and convert them to dictionaries or JSON. This is useful for sending data over the network or saving it to a file.

pydantic model | -> python dictonary
               | -> JSON string
               | -> XML
'''

from pydantic import BaseModel, ConfigDict # type: ignore[reportMissingImports]: 
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S")}
    )


user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    created_at=datetime(2024, 6, 1, 12, 0, 0),
    address=Address(street="123 Main St", city="Anytown", zip_code="12345"),
    is_active=False,
    tags=["premium", "subscriber"]
)

# Convert to dictionary
python_dict = user.model_dump()  # Convert to dictionary
print("Python Dictionary:", python_dict)

print("=========="*20)

# Convert to JSON string
json_string = user.model_dump_json()  # Convert to JSON string
print("JSON String:", json_string)