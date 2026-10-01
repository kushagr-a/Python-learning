class ChaiOrder:
    # __init__ hi Python mein "Constructor" hota hai.
    # Constructor ek special function hai jo tab automatic chal jata hai (call hota hai) 
    # jab hum class se naya object banate hain.
    # Kab use karein? Jab hum chahte hain ki object bante hi usme kuch initial data set ho jaye.
    def __init__(self, type_, size):
        # 'self' us naye object ko point karta hai jo abhi ban raha hai.
        # Yahan hum naye object (jaise ki hamara 'order') ke andar properties set kar rahe hain.
        self.type = type_
        self.size = size
    
    # Yeh ek normal method hai jo class mein function ka kaam karta hai
    def summary(self):
        return f"Aapne {self.type} order ki hai, jiski size {self.size} ml hai."
    

# Yahan par object (order) ban raha hai. 
# Jaise hi hum ChaiOrder() likhte hain, andar hi andar __init__ function automatic run ho jata hai.
# "ginger chai" aur 150 sidhe __init__ ke (type_, size) arguments mein chale jayenge.
order = ChaiOrder("ginger chai", 150)

# Ab hum us order ki details print kar rahe hain
print(order.summary())