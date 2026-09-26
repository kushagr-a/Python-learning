# here we are study about the scopes and name resolution in python
# there are four types of scopes in python
# 1. Local scope: inside a function or block of code
# 2. Enclosing scope: from outter function if nested
# 3. Global scope: from the top level of the module
# 4. Built-in scope: from the built-in names in python


def serve_chai():
    chai_type = "Masala Chai"  # this variable is in local scope
    print(f"Inside function: {chai_type}")


chai_type = "Green Tea"  # this variable is in global scope
serve_chai()  # calling the function to serve chai
print(f"Outside function: {chai_type}")  # printing the global variable
