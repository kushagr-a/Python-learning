# Notes: `global` ka use tab karte hain jab function ke andar se bahar bane
# variable ko update karna ho. `nonlocal` ka use nested function mein hota hai,
# jahan inner function outer function ke variable ko update karta hai.

# 1. Global Keyword:
# Ye global variable hai, kyunki ye function ke bahar define hua hai.
name = "kushagra"

def nameCalling():
    # `global name` batata hai ki yahan naya local variable nahi banana;
    # bahar wale global `name` ko hi update karna hai.
    global name
    name = "Bharti"
    print(f"Inside the function: {name}")

nameCalling()
# Function ke baad global `name` ki value "Bharti" ho chuki hai.
print(f"Outside the function: {name}")


# 2. Nonlocal Keyword:
def outer_function():
    # Ye `outer_function` ka local variable hai.
    name = "Atul"
    print("Name before using nonlocal:", name)

    # Ye outer function ke andar bana hua nested/inner function hai.
    def inner_function():
        # `nonlocal name` outer function ke `name` ko refer karta hai;
        # isliye assignment outer wala variable update karegi, inner local nahi.
        nonlocal name
        name = "Aman"
        print("Name inside inner function:", name)

    inner_function()
    # Inner function ne outer ka `name` update kiya, isliye yahan "Aman" milega.
    print("Name after using nonlocal:", name)

outer_function()