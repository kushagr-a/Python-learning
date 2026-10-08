class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water  , milk , sugar , chai"

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

# static method ka use tab karte hai jab koi object use karne ke need na ho
# mtlb ki they not depended upon object creation