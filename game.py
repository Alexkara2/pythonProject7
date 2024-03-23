import random
job_list={
    "Java developer":{"salary":50, "gladness_less": 10},
    "Python developer":{"salary":40, "gladness_less": 3},
    "C++ developer":{"salary":45, "gladness_less": 25},
    "Swift developer":{"salary":60, "gladness_less": 12},
}
brand_list={
    "BMW":{"fuel":100, "help":100, "consumption":6},
    "Lada":{"fuel":50, "help":40, "consumption":10},
    "Volvo":{"fuel":70, "help":150, "consumption":8},
    "Ferrari":{"fuel":80, "help":120, "consumption":14},
}
class Start():
    def __init__(self):
        self.mess=0
        self.food=0
        self.name = input("Name:")
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.help = brand_list[self.brand]["help"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
class Human(Start):
    def drive(self):
        if self.help > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.help -= 1
            return True
        else:
            print("The car cannot move")
            return False
    def eat(self):
        if self.food<=0:
            self.shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
            else:
                self.to_repair()
                return
        self.money+=self.salary
        self.gladness-=self.gladness_less
        self.satiety-=4
    def work(self):
        if self.drive():
            pass
        else:
            if self.fuel<20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
    def shopping(self,manage):
        if self.drive():
            pass
        else:
            if self.fuel<20:
                manage="fuel"
            else:
                self.to_repair()
                return
        if manage=="fuel":
            print("I bought fuel")
            self.money-=199
            self.fuel+=100
        elif manage=="food":
            print("Bought food")
            self.money-=50
            self.food+=50
        elif manage=="delicacies":
            print("Hooray! Delicious!")
            self.gladness+=10
            self.satiety+=2
            self.money-=15
    def chill(self):
        self.gladness+=10
        self.mess+=5
    def clean_home(self):
        self.gladness-=5
        self.mess=0
    def to_repair(self):
        self.help+=100
        self.money-=50
    def days_indexes(self,day):
        day=f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}","\n")
        human_indexes=self.name+"'s indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money-{self.money}")
        print(f"Satiety-{self.satiety}")
        print(f"Gladdness-{self.gladness}")
        home_indexes="Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food-{self.food}")
        print(f"Mess-{self.mess}")
        car_indexes=f"{self.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel-{self.fuel}")
        print(f"Strenght-{self.help}")
    def is_live(self):
        if self.gladness<0:
            print("Depression...")
            return False
        if self.satiety<0:
            print("Dead")
        if self.money<-500:
            print("Bankrupt...")
            return False
        return True
    def live(self, day):
        self.days_indexes(day)
        dice=random.randint(1, 4)
        if self.satiety<20:
            print("I'll go eat")
            self.eat()
        elif self.gladness<20:
            if self.mess>15:
                print("I want to chill, but there is so much mess...\n"
                      "So I will clean the house")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money<0:
            print("Start working")
            self.work()
        elif self.help<15:
            print("I need to repair my car")
            self.to_repair()
        elif dice==1:
            print("Let's chill!")
            self.chill()
        elif dice==2:
            print("Start working")
            self.work()
        elif dice==3:
            print("Cleaning time!")
            self.clean_home()
        elif dice==4:
            print("Time for treats!")
            self.shopping("delicacies")



nick = Human()

for day in range(1, 10):
    nick.live(day)