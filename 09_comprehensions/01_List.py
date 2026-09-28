# shoter way of writting a code 
# comprehensions are a concise way to create lists,sets,dictionaries, or generators in py using a single line of code.
# where are they used in Real life -> Filter items, trasnsform item, create a new collection, flatten nested
# types -> List, Set, Dictionary, Generator

menu = [
    "Masala chai",
    "Iced Americano",
    "Cappuccino",
    "Espresso",
    "Latte",
    "Dalgona Coffee",
    "Cold Brew"
]


# normal way to print 
# for item in menu:
#     print(item)

# list comprehension
# filtering that on the basis of condition and always used if 
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

name = [
    "Jhon",
    "wave",
    "Rama",
    "Raju",
    "Kushu"
]

printed_Names = [pName for pName in name if len(pName) < 5 ]
print(printed_Names)