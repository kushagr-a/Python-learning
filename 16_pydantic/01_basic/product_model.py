from pydantic import BaseModel  # type: ignore[reportMissingImports]

class Product (BaseModel):
    id: int
    name: str
    price:float
    in_stock:bool = True


Product_one = Product(
    id = 101,
    name = "Apple",
    price = 109.99,
    in_stock = True
)

product_two= Product(
    id = 102,
    name = "Mango",
    price = 109.99,
)

# this is wrong way to do 

# product_three = Product(
#     name="keyboard"
# )

# way to print the product details
print(Product_one)
print(product_two)

# where we use **kwargs for printing the product details