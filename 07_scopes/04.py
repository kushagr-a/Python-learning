chai_type = "plain"  # Global scope

def front_desk():
    def kitchen():
        global chai_type  # referring to the global scope variable
        chai_type = "Masala Chai"  # updating the variable in the global scope
    kitchen()  # calling the inner function to update the chai type


front_desk()  # calling the outer function to update chai
print(f"Global scope: {chai_type}")  # printing the global variable