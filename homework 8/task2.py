a = 100
b = 999

res = 0
for i in range(a, b + 1):
    d = {}
    for j in str(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    print(d)
    for w in str(i):
        if d[w] == 2:
            res += 1
            break


print(res)