# when u want unique one then go to the set comprehension

fav_chai = [
    "Masala chai", "Green tea","Black tea",
    "Iced Americano","Green tea","Black tea","Latte",
]

fav_tea = {chai for chai in fav_chai if len (chai) > 10 }
print(fav_tea)

recipes = {
    "masala_chai": ["ginger", "cardamom", "cloves"],
    "Elachi_tea": ["cardamom", "cinnamon", "black tea"],
    "masala_doodh": ["milk", "sugar", "cardamom", "cloves"],
}

unique_Spices = {spice for incredient in recipes.values() for spice in incredient}
print(unique_Spices)