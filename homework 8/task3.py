a = 100
b = 9999

res = 0
for i in range(a, b + 1):
    d = {}
    tmp = 0
    for j in str(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

    print(d)
    for w in str(i):
        if d[w] > 1:
            break
        else:
            tmp += 1

    if tmp == len(str(i)):
        res += 1

print(res)