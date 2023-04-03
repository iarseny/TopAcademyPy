from random import randint

l1 = [randint(-1000, 1000) for i in range(randint(1, 10))]
l2 = [randint(-1000, 1000) for j in range(randint(1, 10))]

answer1 = []

for i in l1:
    answer1.append(i)
    
for j in l1:
    answer1.append(j)
    
    
print(answer1)
