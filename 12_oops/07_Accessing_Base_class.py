# ==============================================================
# OOPs Concepts: Accessing Base Class Constructor (__init__)
# ==============================================================

# Yeh hamari parent class (Base class) hai
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# --------------------------------------------------------------
# 1st way: NO BASE CLASS CALL (Code Repeat ho raha hai)
# --------------------------------------------------------------
# Is tarike mein humne virasat (inheritance) ka actual fayda nahi uthaya. 
# Jo properties (type_, strength) Parent handle kar sakta tha, hum wahi same 
# code child class mein wapas likh rahe hain. Yeh tarika recommended nahi hai.

# class GingerChai(Chai):
#     def __init__(self,type_, strength, spice_level):
#         self.type = type_           # Repetition
#         self.strength = strength    # Repetition
#         self.spice_level = spice_level


# --------------------------------------------------------------
# 2nd way: EXPLICIT CALL (Direct class ka naam le kar bulana)
# --------------------------------------------------------------
# Yahan hum explicitly/specifically bata rahe hain ki "Chai" class ka __init__ call karo.
# Jab hum aise class ka naam directly likhte hain, toh 'self' pass karna lazmi (compulsory) hota hai.
# Problem: Agar future mein parent class ka naam 'Chai' se badal kar 'HotDrink' ho gaya, 
# toh aapko yahan aakar bhi naam manually change karna padega.

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)  # Explicitly calling Parent's __init__
#         self.spice_level = spice_level


# --------------------------------------------------------------
# 3rd way: IMPLICIT CALL using super() (Best & Modern Way)
# --------------------------------------------------------------
# Yeh sabse best aur modern (Python 3+) tarika hai.
# super() ek smart function hai. Yeh automatically khud dhundh leta hai ki iski Parent class 
# kaunsi hai (yahan 'Chai') aur uska __init__ apne aap (implicitly) call kar deta hai.
# Fayde: 
# 1. Aapko 'self' pass karne ki zaroorat NAHI padti.
# 2. Agar parent class ka naam kal badal gaya, toh yahan kuch change nahi karna padega.

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # super() ne bina naam liye indirectly (implicitly) base class ke __init__ ko call kiya
        super().__init__(type_, strength)
        # Ab jo extra property is child ki thi, wo yahan set kar di:
        self.spice_level = spice_level


# ==============================================================
# EXECUTION TEST
# ==============================================================

ginger = GingerChai("Regular", "Strong", "Extra Strong")

# Print karke check karte hain. Parent wale variables aur child wala variable, sab properly set huye.
print(f"Chai Type (Parent se aaya): {ginger.type}")
print(f"Chai Strength (Parent se aaya): {ginger.strength}")
print(f"Spice Level (Child ka apna): {ginger.spice_level}")
 