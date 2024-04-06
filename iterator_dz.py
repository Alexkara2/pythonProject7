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