def  local_chai():
    yield "Masala chai"
    yield "ginger Chai"

def imported_chai():
    yield "Korean Mint Chai"
    yield "Green Tea Chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    print("stall Open")
    try:
        while True:
            order = yield "wating for chai"
    except:
        print("stall Closed")

stall = chai_stall()
print(next(stall))
stall.close() # clenup memory its important