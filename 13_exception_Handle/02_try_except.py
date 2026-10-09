chai_menu = {'masala':30, 'ginger':40}

try:
    print(chai_menu['elaichi'])

except KeyError:
    print("Please select a valid chai from the menu")

print("Thank you for visiting")

# output -> key error   