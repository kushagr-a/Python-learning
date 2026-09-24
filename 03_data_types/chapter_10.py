# here we are study about dictionaries in python
# () is used to define a dictionary

chai_order = dict(type="Ginger Chai", size="Medium", sugar_level=3)
print(f"Chai Order: {chai_order}")

# accessing values in a dictionary
print(f"Chai Type: {chai_order['type']}")
print(f"Chai Size: {chai_order['size']}")
print(f"Chai Sugar Level: {chai_order['sugar_level']}")

chai_recepie = {} # another way to define a dictionary

chai_recepie["base"] = "Ginger Chai"
chai_recepie["liquide"] = "milk"

print(f"Chai Recepie: {chai_recepie ['base']}")
del chai_recepie["liquide"] # deleting a key-value pair from the dictionary
print(f"Chai Recepie after deletion: {chai_recepie}")

chai_order = dict(type="Ginger Chai", size="Medium", sugar_level=3)
print(f"Chai Order: {chai_order.keys()}")  # getting all the keys in the dictionary
print(f"Chai Order: {chai_order.values()}")  # getting all the values in the dictionary
print(f"Chai Order: {chai_order.items()}")  # getting all the key-value pairs in the dictionary