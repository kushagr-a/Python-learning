from pydantic import BaseModel  # type: ignore[reportMissingImports]
from typing import Optional, List, Dict


class Cart(BaseModel):
    user_id: int
    items: List[str]  # list of strings
    quantity: Dict[str, int]  # key is string and value is int


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # optional field with default value None


cart_data = {
    "user_id": 101,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantity": {"Laptop": 1, "Mouse": 2, "Keyboard": 1},
}


# `Cart(**cart_data)` me `**` dictionary unpacking karta hai.
#
# Python ise internally iske barabar samajhta hai:
#
# Cart(
#     user_id=101,
#     items=["Laptop", "Mouse", "Keyboard"],
#     quantity={"Laptop": 1, "Mouse": 2, "Keyboard": 1},
# )
#
# `cart_data` ki keys aur Cart ke field names same hain, isliye `**` use
# karke dictionary ko keyword arguments me automatically convert kar sakte hain.
# Pydantic in values ko model ke type ke according validate bhi karta hai.

cart = Cart(**cart_data)
print(cart)


# ============================================================
# Cart banane ke alag-alag common tareeqe
# ============================================================

# 1. Dictionary unpacking: short aur convenient.
cart_1 = Cart(**cart_data)

# 2. Explicit keyword arguments: zyada clear, lekin verbose.
cart_2 = Cart(
    user_id=cart_data["user_id"],
    items=cart_data["items"],
    quantity=cart_data["quantity"],
)

# 3. Pydantic v2: dictionary/object ko validate karke model banana.
# API, database ya kisi external source se dictionary aaye to ye useful hai.
cart_3 = Cart.model_validate(cart_data)

# 4. Pydantic v1 ka purana equivalent:
# cart_4 = Cart.parse_obj(cart_data)
# Pydantic v2 me `model_validate()` preferred hai.

# 5. JSON string se model banana (Pydantic v2):
cart_json = """
{
    "user_id": 101,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantity": {"Laptop": 1, "Mouse": 2, "Keyboard": 1}
}
"""
cart_5 = Cart.model_validate_json(cart_json)

# Pydantic v1 me JSON ke liye purana equivalent:
# cart_6 = Cart.parse_raw(cart_json)


# `Cart(cart_data)` mat likhna:
# Cart(cart_data)
#
# Isme poori dictionary ko positional argument ki tarah pass kiya jata hai.
# Pydantic models ko fields generally keyword arguments ke roop me chahiye,
# isliye `Cart(**cart_data)` ya `Cart.model_validate(cart_data)` use karein.


# Yaad rakhne ka shortcut:
#
# `*`  -> list/tuple unpack karta hai
# `**` -> dictionary ko keyword arguments me unpack karta hai
#
# Example:
# values = [1, 2]
# print(*values)                 # print(1, 2)
#
# data = {"name": "Kushagra", "age": 25}
# some_function(**data)          # some_function(name="Kushagra", age=25)
