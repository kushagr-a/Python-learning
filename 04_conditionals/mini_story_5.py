#  here learning about ternary operator in python

oder_amt = int(input("Enter your order amount: "))  # this is the way to take user input in python and convert it into integer

print("Free Delivery" if oder_amt >= 300 else "30 rupees delivery charge" ) # this is the way to use ternary operator in python

#  another way 
delivery_fees = 0 if oder_amt >= 300 else 30
print(f"Delivery fees: {delivery_fees} rupees")