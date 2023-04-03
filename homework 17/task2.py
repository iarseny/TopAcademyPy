from random import randint
l = [randint(-1000, 1000) for i in range(randint(1, 10))]

otr = 0
pol = 0
zero = 0

for i in l:
    if i < 0:
        otr += 1
    elif i > 0:
        pol += 1
    else:
        zero += 1

print(min(l), max(l), otr, pol, zero)

