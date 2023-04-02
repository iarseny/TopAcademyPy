size = int(input())

s = [int(input()) for i in range(size)]

otr = 0
chet = 0
nechet= 0
if len(s) >= 3:
    krat_3 = s[3]
else:
    krat_3 = 0

maximum = [s[0], 0]
minimum = [s[0], 0]

for j, i in enumerate(s):
    if i < 0:
        otr += 1

    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1

    if j % 3 == 0 and j != 3 and len(s) >= 3:
        krat_3 *= i

    if i > maximum[0]:
        maximum[0] = i
        maximum[1] = j

    if i < minimum[0]:
        minimum[0] = i
        minimum[1] = j


sum = 0
if minimum[1] < maximum[1]:
    for i in range(minimum[1] + 1, maximum[1]):
        sum += s[i]

else:
    
    for i in range(maximum[1] + 1, minimum[1]):
        sum += s[i]


print(otr, chet, nechet, krat_3, minimum[0] * maximum[0], sum)