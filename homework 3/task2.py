a = [int(input()) for i in range(3)]

find = input()

if find == "max":
    max = a[0]
    for i in a:
        if i > max:
            max = i
    print(max)
elif find == "min":
    min = a[0]
    for i in a:
        if i < min:
            min = i
    print(min)
else:
    sum = 0
    for i in a:
        sum += i
    print(sum / len(a))