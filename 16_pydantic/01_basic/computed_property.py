from pydantic import BaseModel, computed_field, Field # type: ignore[reportMissingImports]

# Example of a Pydantic model with a computed property
class product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float: 
        return self.price * self.quantity

# Example usage
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=1, description="Number of nights for the booking")
    rate_per_night: float

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=150.0)
print(f"Total cost for booking: ${booking.total_cost}")

print("This is the booking data:",booking.model_dump())  # This will include the computed field 'total_cost' in the output