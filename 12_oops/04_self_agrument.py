class Chaicup:
    size = 150 #ml


    def describe(self):
        return f"Chai cup of size {self.size} ml"


mug = Chaicup()
print(mug.describe())
print(Chaicup.describe(mug))