from pydantic import BaseModel # type: ignore[reportMissingImports]
from typing import Optional, Field
import re

class Employee(BaseModel):
    id:int
    name:str = Field(
        ..., # ... means this field is required
        min_length=3,
        max_length=50,
        description="Employee's name",
        example="John Doe"
    )
    department: Optional[str] = 'General'  # default value is 'General'
    salary: float = Field(
        ...,  # required field
        gt=0,  # greater than 0
        description="Employee's salary",
        example=50000.0
    )

# validation example with regular expression for email and phone number
class User (BaseModel):
    email: str = Field(
        ...,  # required field
        regex=r'^\S+@\S+\.\S+$',  # simple email regex
        description="User's email address",
        example="john.doe@example.com"
    )
    phone:str = Field(
        ...,  # required field
        regex=r'^\+?\d{10,15}$',  # simple phone number regex
        description="User's phone number",
        example="+1234567890"
    )
    age: int = Field(
        ...,  # required field
        ge=0,  # greater than or equal to 0
        le=120,  # less than or equal to 120
        description="User's age",
        example=30
    )
    discount: float = Field(
        ...,
        ge=0.0,  # greater than or equal to 0.0
        le=100.0,  # less than or equal to 100.0
        description="User's discount percentage",
        example=10.5
    )