# Class method aur static method ka practical example.
#
# Yaad rakhne ka short rule:
# - Normal method: self leta hai -> object ke data par kaam karta hai.
# - Class method: cls leta hai -> class ko use karke object banata/configure karta hai.
# - Static method: self/cls kuch nahi leta -> class se related independent utility hota hai.

class ChaiOrder:

    # __init__ normal/instance method hai.
    # Jab bhi ChaiOrder ka object banega, Python is method ko automatically call karega.
    # self current object ko represent karta hai.
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # @classmethod decorator method ko class method bana deta hai.
    # Is method ka pehla parameter "cls" hota hai, jo current class
    # (yahan ChaiOrder) ko represent karta hai.
    #
    # Ye alternate constructor/factory method hai:
    # dictionary se data lekar ChaiOrder ka object banata hai.
    # Jab input dictionary, JSON ya database record ke form mein ho,
    # tab aisa method bahut useful hota hai.
    @classmethod
    def from_dic(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    # Ye bhi class method hai, lekin input string ke form mein leta hai.
    # "ginger-less_sugar-small" ko split karke 3 values banata hai
    # aur cls(...) ke through naya ChaiOrder object return karta hai.
    #
    # cls(...) likhne ka fayda:
    # agar future mein ChaiOrder ki child class is method ko call kare,
    # to object child class ka banega. Isliye classmethod mein cls use karte hain.
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

    # @staticmethod mein self ya cls nahi hota.
    # Is method ko object ke data (self) ya class ke data (cls) ki zaroorat nahi hai.
    # Bas chai order se related ek helper/utility operation hai.
    #
    # Static method kab use karein?
    # Jab function logically class ke andar belong karta ho,
    # lekin use object/class ki state ki zaroorat na ho.
    # Example: size valid hai ya nahi, ye check karna.
    #
    # Isko ChaiOrder.is_valid_size("large") ke form mein call kar sakte hain.
    # Ismein Python koi hidden self ya cls pass nahi karta.
    @staticmethod
    def is_valid_size(size):
        valid_sizes = ("small", "medium", "large")
        return size in valid_sizes


# Class method ko class ke naam se call kar rahe hain.
# from_dic dictionary ko samajhkar object banane ka alternate tareeka hai.
order1 = ChaiOrder.from_dic(
    {"tea_type": "masala", "sweetness": "medium", "size": "large"}
)

# Ye bhi class method hai, par is baar source data string hai.
order2 = ChaiOrder.from_string("ginger-less_sugar-small")

# Normal constructor: data directly __init__ ke expected order mein diya.
order3 = ChaiOrder("green", "medium", "large")

# Static method ka call: isko object banaye bina directly class se use kiya.
print(ChaiOrder.is_valid_size(order1.size))  # True
print(ChaiOrder.is_valid_size("extra-large"))  # False

# __dict__ object ke instance attributes ko dictionary ke form mein dikhata hai.
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

# Class method vs static method - one-line revision:
# classmethod -> cls milta hai, class/object create ya configure karne mein useful.
# staticmethod -> self/cls nahi milta, class-related independent helper ke liye useful.