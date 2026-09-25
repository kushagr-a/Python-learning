snacks = str(input("Enter your favorite snack: ")).loweer() # this is the way to take user input in python and convert it into string and lower case


if snacks == "cookies" or snacks == "samosa":
    print(f"You'r order {snacks} are confirmed. Please wait for 10 minutes.")
else:
    print(f"show unavailability")