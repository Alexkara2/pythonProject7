import datetime
from datetime import timedelta

time1 = datetime.datetime.now()

def calc(n):
    while n!=0:
        n-=1
        yield n
n = int(input("Number:"))
cal = calc(n)
try:
    for i in range(n+1):
        print(next(cal))
except:
    print("Gen is stoped!")

time2 = datetime.datetime.now()
b=time2-time1

try:
    assert b<timedelta(seconds=1)
    print("Test passed successfully!")
except:
    print("Test failed!")