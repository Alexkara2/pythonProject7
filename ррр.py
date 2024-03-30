import inspect
import random
import sys
mes="mama"
a = ["asa", "sas"]

def func():
    pass

print(hasattr(a, "upper"))
print("---------------")
print(callable(func))
print(callable(a))
print("---------------")
class Human():
    def __init__(self):
        self.age=0
class AD(Human):
    def a(self):
        print(self.age)

print(issubclass(AD, Human))
print(issubclass(Human, AD))
print("---------------")

print(inspect.isclass(Human))
print(inspect.ismodule(random))
print(inspect.isfunction(func))
print("---------------")

print(sys.modules)