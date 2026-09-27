def chai_status(cup_left):
    if cup_left == 0:
        return "No chai left"
    return "Chai is available"

# once a retur n function hit then other statements will not be executed
print(chai_status(0))  # Output: No chai left
print(chai_status(5))  # Output: Chai is available

def chai_report():
    return 100, 20, 10 # sold, remaining
sold, remaining, _ = chai_report()  # unpacking the returned tuple
print(f"Sold: {sold}, Remaining: {remaining}")  # Output: Sold: