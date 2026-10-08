# Here we are study about Method resolution order

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Ginger blend"

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)
print(D.mro())