from pydantic import BaseModel, field_validator, model_validator # type: ignore[reportMissingImports]
from datetime import datetime

# Example of field validation using Pydantic's field_validator decorator
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def name_must_be_capitalized(cls, value):
        if not value.istitle(): # istitle() method checks if the first character of each word is uppercase and the rest are lowercase
            raise ValueError('Name must be capitalized')
        return value

# Example of model validation using Pydantic's model_validator decorator
class User (BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower().strip() # lower() method converts the string to lowercase and strip() removes any leading or trailing whitespace


# Example of model validation using Pydantic's model_validator decorator
class Product (BaseModel):
    price: str # $4.44 

    @field_validator('price', mode='before')
    def parse_price(cls, value):
        if isinstance(value, str):
            return float(value.replace('$', '')) # replace() method replaces the $ sign with an empty string and then converts the string to float
        return value

# Example of model validation using Pydantic's model_validator decorator
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('Start date must be before end date')
        return values