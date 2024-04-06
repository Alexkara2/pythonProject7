my_list = [5,8,9]
i = iter(my_list)
print(next(i))
print(next(i))
print(next(i))
print(i)

a_list = {"a":1,
        "b": 2,}

for i in a_list:
    print(i)

a = list(range(1,10))
print(a)

iterator=iter(my_list)
for elem in iterator:
    print(elem)
for elem in iterator:
    print(elem)

m_list = [j for j in range(5, 10)]
for i in m_list:
    print(i)