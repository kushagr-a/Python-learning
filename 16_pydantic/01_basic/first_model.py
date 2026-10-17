
print("start of pydantic journey!!!!!")

from pydantic import BaseModel # type: ignore[reportMissingImports]

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    "id": 101,
    "name": "Kushagra",
    "is_active": True
}

user = User(**input_data)
print(user)