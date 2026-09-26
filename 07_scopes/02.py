def chai_counter():
    chai_order = "lemon"  # Enclosing scope

    def print_order():
        chai_order = "masala"  # Local scope
        print(f"Inside function: {chai_order}")

    print_order()  # calling the inner function to print the order
    print(f"Outside function: {chai_order}")


chai_order = "tulsi"  # Global scope
chai_counter()  # calling the outer function to serve chai
print(f"Global scope: {chai_order}")  # printing the global variable
