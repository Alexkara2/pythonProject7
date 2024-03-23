class Computer:
    def __init__(self):
        self.name = "aksfsd"
        self.name1 = "aksfsd"
    def calculate(self):
        print("calculating")
class Display:
    def display(self):
        print("I display the image")
class SmartPhone(Display, Computer):
    def paly(self):
        print(self.name)
        print(self.name1)

iphone = SmartPhone()
iphone.calculate()
iphone.display()
iphone.paly()