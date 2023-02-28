s = []

a = input()

for i in a:
    s.append(i)

s.reverse()

res = ""

for i in s:
    res += i

print(res)