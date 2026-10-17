from pydantic import BaseModel, field_validator, model_validator # type: ignore[reportMissingImports]

# Example of field validation using Pydantic's field_validator decorator
class User(BaseModel):
    username: str

    email: str

    @field_validator('username')
    def validate_username(cls, value): # cls class ko represent karta hai aur value field ka value hai
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if not value.isalnum():
            raise ValueError('Username must be alphanumeric')
        return value

    @field_validator('email')
    def validate_email(cls, value): # cls class ko represent karta hai aur value field ka value hai
        if '@' not in value:
            raise ValueError('Email must contain @ symbol')
        return value


# Example of model validation using Pydantic's model_validator decorator
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values): # cls class ko represent karta hai aur values model ke saare fields ka dictionary hai
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values
