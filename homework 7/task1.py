a = int(input())
b = int(input())

nine = []
chetnie = []
nechetnie = []

for i in range(a, b + 1):
    if i % 9 == 0:
        nine.append(i)
    if i % 2 == 0:
        chetnie.append(i)

    if i % 2 != 0:
        nechetnie.append(i)

y = lambda x: sum(x) / len(x)

print(sum(nine), sum(chetnie), sum(nechetnie), y(nine), y(chetnie), y(nechetnie))