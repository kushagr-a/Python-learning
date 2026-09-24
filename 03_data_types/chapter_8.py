# learning about list data types in python
# [] is used to define a list
#  mutable

ingrediernts = ["Ginger", "Cinnamon", "Cardamom"]

ingrediernts.append("Cloves")  # adding an element to the list
print(f"Ingredients: {ingrediernts}")

ingrediernts.remove("Cinnamon")  # removing an element from the list
print(f"Ingredients after removal: {ingrediernts}")

ingrediernts.insert(3, "Nutmeg")  # inserting an element at a specific index
print(f"Ingredients after insertion: {ingrediernts}")

last_added = ingrediernts.pop()  # removing the last element from the list
print(f"Last added ingredient: {last_added}")
print(f"Ingredients after popping: {ingrediernts}")

# sorting the list
ingrediernts.sort()  # sorting the list in ascending order
print(f"Sorted Ingredients: {ingrediernts}")

sugar_lvl = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_lvl)}")  # finding the maximum value in the list

# operator overloading in list
list1 = ["water", "milk"]
list2 = ["sugar", "honey"]
combined_list = list1 + list2  # concatenating two lists
print(f"Combined List: {combined_list}")

strong_tea = ["tea"] * 3  # repeating the list elements
print(f"Strong Tea: {strong_tea}")

# byteArray data type in python
# byteArray is a mutable sequence of bytes
byte_array = bytearray(b"Hello World")
print(f"Byte Array: {byte_array}")