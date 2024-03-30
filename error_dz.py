result = []
try:
    def divider(a, b):
         if a < b:
             raise ValueError
         if b > 100:
             raise IndexError
         if b==0:
             raise ZeroDivisionError
         return a/b
    data = [10, 2, 2, 5, 123, 4, 18, 0, 15, 8, 4]
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print(result)