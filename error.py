
try:
    a = int(input("1:"))
    b = int(input("2:"))
    print(a/b)
except ValueError:
    print("? Ne to vvodish!")
except ZeroDivisionError:
    print("? Dilish na nul!")
finally:
    print("Nu vrode norm!")

print("End")



