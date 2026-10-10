class InvalidChiaError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 10, "elachi": 10}
    try:
        if flavor not in menu:
            raise InvalidChiaError("That chai is not in the menu")
        if not isinstance(cups, int) or cups < 1:
            raise TypeError("Quantity must be a positive number")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} {flavor} chai is {total} rupees")
    except InvalidChiaError as e:
        print(e)
    except TypeError as e:
        print(e)
    finally:
        print("Thanks for visiting chai sutta bar")



bill("masala", "two")
# output -> Quantity must be a positive number

bill("cardmom", 5)
# output -> That chai is not in the menu

bill("masala", 5)
# output -> Your bill for 5 masala chai is 100 rupees