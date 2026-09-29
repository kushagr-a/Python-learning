# yield also used for send a data or generate the data

def chai_customer():
    print("welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"preparing {order}")
        order = yield

stall = chai_customer()
next(stall) # start generator before receiving the input
# stall.send("Masala chai")
stall.send("Ginger chai")
stall.send("Lemon chai")