# here study about tuples in python
# () is used to define a tuple
# this is immutable data type, which means we cannot change the values of a tuple once it is created

masala_chai = ("Ginger", "Cinnamon", "Cardamom")

spieces, flavor, aroma = masala_chai  # unpacking the tuple into variables
print(f"Spices: {spieces}, Flavor: {flavor}, Aroma: {aroma}")


# memebership operator in tuple
print("Ginger" in masala_chai)  # True