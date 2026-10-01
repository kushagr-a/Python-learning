# Each object has own entity

class chai:
    # properties
    origin = "India"
    price = 20
    
print(chai.origin)
print(chai.price)

chai.is_hot = True
print(chai.is_hot)

# creating objects from class chai

masala = chai()
print(masala.price)
print(masala.is_hot)