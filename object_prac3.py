class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Dog(Animal):
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

Pochi = Dog("Pochi", 5, "black")

print(Pochi.name, ":", "weight", Pochi.weight, "kg", "color", Pochi.color)