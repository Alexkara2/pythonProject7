class Animal:
    def __init__(self):
        self.hunger=0
class Mammals(Animal):
    def Hunter(self):
        self.hunger+=20
class NoMammals(Animal):
    def Eat(self):
        self.hunger+=10

fish = NoMammals()
trx=Mammals()
print(fish.hunger)
print(trx.hunger)
fish.Eat()
trx.Hunter()
print(fish.hunger)
print(trx.hunger)
