class Chai:
    # Yeh ek class attribute hai. Sabhi Chai objects ke liye by default "hot" hoga.
    temperature = "hot" 

# Ek object banate hai
cutting = Chai()

# Abhi yahan class attribute access ho raha hai kyunki object ke paas apna attribute nahi hai
print("Shuruwat mei temperature:", cutting.temperature)  # Output: hot

# Ab hum object (cutting) ke liye ek naya attribute set kar rahe hai.
# Yeh naya instance attribute ab class wale attribute ko "shadow" (chhupa) dega.
cutting.temperature = "warm"

# Ab jab hum print karenge, toh instance (object) ka apna attribute print hoga, na ki class wala.
# Isko hi Attribute Shadowing kehte hai.
print("Shadow karne ke baad temperature:", cutting.temperature)  # Output: warm

# Class attribute abhi bhi waisa hi hai, bas is object ke liye chhip gaya hai.
print("Class ka apna temperature abhi bhi:", Chai.temperature) # Output: hot

# but when we delete the instance attribute
del cutting.temperature
print("After deleting instance attribute:", cutting.temperature) # Output: hot
