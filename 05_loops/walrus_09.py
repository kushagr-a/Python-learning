# here we are study about walrus operator in python
# := is the walrus operator

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")