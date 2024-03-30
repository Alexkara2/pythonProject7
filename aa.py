class HeightError(Exception):
    pass
class AgeError(Exception):
    pass


age = int(input("Age:"))
height = int(input("Height:"))

try:
    if height>270 or height<170:
        raise HeightError
    elif age<20 or age>60:
        raise AgeError
except HeightError:
    print("Height Error!")
except AgeError:
    print("Age Error!")
else:
    print("Wellcome!")

#__str__(self) - утворити свій вийняток