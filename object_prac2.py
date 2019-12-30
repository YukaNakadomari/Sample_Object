"""class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + " is eating " + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping...")

fluff = Cat("Fluff", 4.5)

print(fluff.weight)

fluff.eat("tuna")
fluff.eatAndSleep("sakana")
print(fluff.weight)"""

class dog:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
        print(name, weight, color)

    def eat(self, food):
        if food == "beef":
            self.weight = self.weight + beef.weight
        elif food == "pork":
            self.weight = self.weight + pork.weight
        elif food == "chicken":
            self.weight = self.weight + chicken.weight
        else:
            pass
        print(self.name + " is eating " + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping...")


Pochi = dog("Pochi", 5, "black")
Choco = dog("Choco", 3, "brown")
Siro = dog("Siro", 4, "white")


class food:
    def __init__(self, fweight):
        self.weight = fweight


beef = food(0.6)
pork = food(0.8)
chicken = food(0.3)

Pochi.eat("beef")
Pochi.eatAndSleep("pork")
print("Pochi.weight", Pochi.weight)

Choco.eat("beef")
Choco.eatAndSleep("chicken")
print("Choco.weight", Choco.weight)

Siro.eat("pork")
Siro.eatAndSleep("chicken")
print("Siro.weight", Siro.weight)