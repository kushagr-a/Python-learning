# Printing and returning the values are two different things. 
# If you want to return a value from a function, you should use the return statement. 
# If you want to print a value to the console, you should use the print function.

def calculate_bill(cups, price_per_cup):
    total = cups * price_per_cup
    return total  # returning the value instead of printing it

calculated_bill = calculate_bill(3, 5)  # calling the function and storing the returned value
print(f"The total bill is: {calculated_bill}")  # printing the returned value