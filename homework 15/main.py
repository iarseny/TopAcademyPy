from random import randint
size = int(input())

res = [randint(-1000, 1000) for i in range(size)]

Q1 = [i for i in res if i % 2 == 0]
Q2 = [i for i in res if i % 2 != 0]
Q3 = [i for i in res if i < 0]
Q4 = [i for i in res if i > 0]


print(Q1, Q2, Q3, Q4)
