# we are study about sets in python
# {} is used to define a set

essential_ingredients = {"Ginger", "Cinnamon", "Cardamom"}
optional_ingredients = {"Cloves", "Cinnamon", "Saffron"}

all_spices = essential_ingredients | optional_ingredients  # union of two sets
print(f"All Spices: {all_spices}")

# intersection of two sets
common_spices = essential_ingredients & optional_ingredients
print(f"Common Spices: {common_spices}")

# only in essential_ingredients but not in optional_ingredients
unique_essential = essential_ingredients - optional_ingredients
print(f"Unique Essential Spices: {unique_essential}")

# memebership test in set
print("Ginger" in essential_ingredients)  # True
print("Ginger" in optional_ingredients)  # False

# if u are to freez any set so we are used frozenset() function to make it immutable
frozen_essential_ingredients = frozenset(essential_ingredients) # making the set immutable