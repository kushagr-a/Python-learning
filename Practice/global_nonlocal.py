# Here we are practicing the use of global and nonlocal keywords in Python.

# 1. Global Keyword:
name = "kushagra" # idhr mene gloibal variable banya 

def nameCalling():
    global name  # Referring to the global variable 'name'
    name = "Bharti" # idhr mene global variable ko update kiya
    print(f"Inside the function: {name}")  # This will print the local variable 'name'

nameCalling()  # Calling the function
print(f"Outside the function: {name}")  # This will print the global variable 'name'


# 2. Nonlocal Keyword:
def outer_function():
    name = "Atul"  # This is a local variable in the outer function
    print("Name before using nonlocal:", name)  # This will print the local variable 'name'

    # Nested function
    def inner_function():
        nonlocal name  # Referring to the variable 'name' in the outer function
        name = "Aman"  # Updates the variable in the outer function
        print("Name inside inner function:", name) # this will print aman cause this is a local variable in the inner function

    inner_function()
    print("Name after using nonlocal:", name) # but this will print aman cause this is a local variable in the outer function

outer_function()  # Calling the outer function