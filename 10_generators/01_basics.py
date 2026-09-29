# generators always come up with yield keyword
# you save memory
# you don't want the result immedietely
# lazy evaluation

def serve_Chai():
    yield "cup 1 Masala chai"
    yield "cup 2 Ginger chai"
    yield "cup 3 Elaichi chai"
    yield "cup 4 Green chai"
    yield "cup 5 lemon chai"

stall = serve_Chai()
for cup in stall:
    print(cup)