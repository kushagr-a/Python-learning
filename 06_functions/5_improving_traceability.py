def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100  # returning the value instead of printing it

oders = [100, 150, 200, 250]  # list of order prices

for price in oders:
    total_price = add_vat(price, 10)  # calling the function and storing the returned value
    print(f"The total price including VAT is: {total_price}")  # printing the returned value