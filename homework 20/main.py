def create_list():
    size = int(input())

    s = [int(input()) for i in range(size)]

    return s


list1 = create_list()
list2 = create_list()

S1 = [i for i in list1 + list2]
print(S1)

S2 = []

for i in list1 + list2:
    if i not in S2:
        S2.append(i)

print(S2)


S3 = []

for i in list1:
    together = False
    for j in list2:
        if j == i:
            together = True

    if together:
        S3.append(i)

print(S3)



S4 = []

for i in list1:
    uniq = True
    for j in list2:
        if j == i:
            uniq = False

    if uniq:
        S4.append(i)


for i in list2:
    uniq = True
    for j in list1:
        if j == i:
            uniq = False

    if uniq:
        S4.append(i)

print(S4)

print([max(list1), max(list2), min(list1), min(list2)])
