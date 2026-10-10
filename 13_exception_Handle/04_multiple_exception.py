def process_order(item, quantity):
    try:
        price = {'masala': 20}[item]
        cost = int(price * quantity)
        print(f"total cost is {cost}")  
    except KeyError:
        print("Please select a valid chai from the menu")
    except (TypeError, ValueError):
        print("Quantity must be a number")

print("Thank you for visiting")

process_order("masala", "two")
# Output -> Quantity must be a number

process_order("elaichi", 5)
# Output -> Please select a valid chai from the menu

process_order("masala", 5)
# Output -> total cost is 100