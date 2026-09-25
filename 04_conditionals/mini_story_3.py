cup_size = str(
    input("Enter your cup size (small, medium, large): ")
).lower()  # this is the way to take user input in python and convert it into string and lower case

if cup_size == "small":
    print("price is 10 rupees")
elif cup_size == "medium":
    print("price is 20 rupees")
elif cup_size == "large":
    print("price is 30 rupees")
else:
    print("Invalid cup size. Please choose from small, medium, or large.")
