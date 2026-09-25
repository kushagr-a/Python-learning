flavours = ["Ginger", "out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue;
    if flavour == "Discontinued":
        break;
    print(f"serving {flavour} chai")    