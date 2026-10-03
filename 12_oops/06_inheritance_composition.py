# ==========================================
# OOPs Concepts: Inheritance & Composition
# ==========================================

# 1. BASE CLASS (Yeh hamara basic template ya blueprint hai)
class baseChai:
    def __init__(self, type_):
        # Jab bhi naya chai object banega, usme 'type' store hoga (jaise "Regular", "Masala")
        self.type = type_

    def prepare(self):
        # Yeh ek normal method (action) hai jo chai banayega
        print(f"Preparing {self.type} chai...")


# 2. INHERITANCE (Virasat/Parent-Child relationship - "IS-A" relationship)
# Yahan 'masalaChai' child class hai, aur 'baseChai' parent class hai.
# Iska matlab masalaChai ek tarah ki baseChai hi hai.
# masalaChai ko 'baseChai' ka pura code (jaise __init__ aur prepare method) free mein mil gaya.
class masalaChai(baseChai): 
    # Humne yahan child class me ek naya/extra feature (method) add kar diya:
    def add_spices(self):
        print("Adding cardamom & ginger to chai...")


# 3. COMPOSITION ("HAS-A" relationship)
# Composition ka seedha matlab hai ki ek class ke andar dusri class ka object rakhna / use karna.
# ChaiShop khud ek Chai NAHI hai (no inheritance), balki ChaiShop ke PAAS ek Chai (object) HAI.
class ChaiShop:
    # Default class set kar di. Ise aage object banane ke liye use karenge.
    chai_class = baseChai # Yeh ek Class reference (Composition) hai.

    def __init__(self):
        # Jab ChaiShop ka naya object banega, toh automatically "Regular" type ki chai ka object ban jayega.
        # self.chai_class("Regular") exactly aise behave karega: baseChai("Regular")
        self.chai = self.chai_class("Regular")

    def serve(self):
        # 'self.chai' actually baseChai (ya masalaChai) ka object hai. 
        # Isliye hum us object ka .prepare() method call kar paa rahe hain.
        print(f"Serving {self.chai} chai in the shop")
        self.chai.prepare()


# 4. INHERITANCE IN CHAI SHOP
# FancyChaiShop ek normal ChaiShop ki hi tarah hai (Inheritance), bas chai alag type ki rakhta hai.
class FancyChaiShop(ChaiShop):
    # Overriding class attribute: Ab yeh Fancy shop 'baseChai' ki jagah 'masalaChai' class use karegi!
    # Jab FancyChaiShop ka object banega, parent (ChaiShop) ka hi __init__ call hoga,
    # lekin 'chai_class' ab masalaChai hone ki wajah se self.chai me masalaChai ka object banega.
    chai_class = masalaChai 


# ==========================================
# FINAL EXECUTION (Kaise kaam kar raha hai dekhte hain)
# ==========================================

print("=== NORMAL SHOP ===")
shop = ChaiShop()
shop.serve() 
# Upar wali line self.chai_class("Regular") -> baseChai("Regular") banayegi.

print("\n=== FANCY SHOP ===")
fancy_shop = FancyChaiShop()
fancy_shop.serve() 
# Fancy shop me chai_class overwrite huyi thi, isliye self.chai_class("Regular") -> masalaChai("Regular") banayegi.

print("\n=== FANCY SHOP EXTRA FEATURE ===")
# Kyunki fancy_shop.chai actually masalaChai ka object hai, hum uska add_spices() function call kar sakte hain.
# Agar yehi cheez shop.chai.add_spices() karte, toh error aata kyunki baseChai me wo function hai hi nahi.
fancy_shop.chai.add_spices()