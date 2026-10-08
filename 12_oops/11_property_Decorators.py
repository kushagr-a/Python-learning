# @property decorator ka use karke normal method ko attribute ki tarah
# read/write kar sakte hain, aur value par validation bhi laga sakte hain.
#
# Simple rule:
# _age = actual/private storage
# age = public property jiske through safe access milega

class TeaLeaf:
    def __init__(self, age):
        # self.age likhne par neeche wala setter call hota hai.
        # Isse object create karte waqt bhi negative age reject hogi.
        self.age = age

    # Getter: leaf.age read karne par ye method automatically call hota hai.
    # User ko internally stored _age directly access karne ki zaroorat nahi.
    @property
    def age(self):
        return self._age

    # Setter: leaf.age = value likhne par ye method automatically call hota hai.
    # Setter ka main use validation, logging ya value transformation ke liye hota hai.
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# Object create karte waqt setter validation run hoti hai.
leaf = TeaLeaf(2)
print(leaf.age)  # Getter call -> 2

# Value update karte waqt bhi setter automatically call hota hai.
leaf.age = 5
print(leaf.age)  # Getter call -> 5

# Is line par ValueError aayega, kyunki age negative allowed nahi hai:
# leaf.age = -1

# Agar __init__ mein self._age = age likhte, to initialization ke time
# setter bypass ho jata aur TeaLeaf(-1) galat value ke saath ban sakta tha.
# Isliye __init__ mein self.age = age use kiya gaya hai.
