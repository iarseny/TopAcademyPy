size = int(input())
res = [int(input()) for i in range(size)]

otr = 0
chet = 0
nechet = 0

index_to_3 = res[0]
minimum = [res[0], 0]
maximum = [res[0], 0]
sum = 0
between = 0
pol = []


for i, j in enumerate(res):
    if j < 0:
        otr += j

    if j % 2 == 0:
        chet += j
    else:
        nechet += j

    if i % 3 == 0 and i != 0:
        index_to_3 *= j

    if j > maximum[0]:
        maximum[1] = i

    if j < minimum[0]:
        minimum[1] = i

    if j > 0:
        pol.append(i)


if maximum > minimum:
    for i in range(minimum[1] + 1, maximum[1]):
        if i == minimum[1] + 1:
            between = res[i]
        else:
            between *= res[i]

else:
    for i in range(maximum[1] + 1, minimum[1]):
        if i == maximum[1] + 1:
            between = res[i]
        else:
            between *= res[i]



for i in range(pol[0] + 1, pol[len(pol) - 1]):
    sum += res[i]


print("Сумма отрицательных:", otr, "Сумма чётных:", chet, "Сумма нечётных:", nechet ,"Произведение с индексами % 3:", index_to_3, "Произведение между минимальным и максимальным:", between, "Сумма:", sum)
