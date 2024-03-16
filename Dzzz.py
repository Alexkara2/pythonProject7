import random
class Animals:
    def __init__(self):
        self.type=input("Type of animal:")
        self.name=input("Name of animal:")
        self.gladness=50
        self.hunger=0
        self.islive=True
    def __del__(self):
        print("Dog is Die!")
        self.islive = False
    def play(self):
        print(f"{self.type},{self.name} playing with you!")
        self.gladness+=10
        self.hunger+=10
    def eating(self):
        print(f"{self.type},{self.name} have lunch time!")
        self.hunger-=10
        self.gladness-=5
    def sleeping(self):
        print(f"{self.type},{self.name} have chill time!")
        self.hunger+=5
        self.gladness+=2
    def is_live(self):
        if self.gladness<0:
            self.__del__()
        elif self.hunger>50:
            self.__del__()
    def progress(self):
        print(f"{self.gladness}=Gladness")
        print(f"{self.hunger}=Hunger")
    def live(self,day):
        self.is_live()
        a=random.randint(1,3)
        print(f"Day of {self.type},{self.name} = {day+1}")
        if a==1:
            self.play()
            self.progress()
        elif a==2:
            self.eating()
            self.progress()
        else:
            self.sleeping()
            self.progress()
Anim=Animals()
for day in range(365):
    if Anim.islive==False:
        break
    else:
        Anim.live(day)