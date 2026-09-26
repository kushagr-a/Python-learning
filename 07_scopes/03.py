def update_chai():
    chai_type = "Masala Chai"  # this variable is in local scope

    def kitchen():
        nonlocal chai_type  # referring to the enclosing scope variable
        chai_type = "Green Tea"  # updating the variable in the enclosing scope
        print(f"Inside kitchen function: {chai_type}")

    kitchen()  # calling the inner function to update the chai type
    print(f"Outside kitchen function: {chai_type}")

update_chai()  # calling the outer function to update chai