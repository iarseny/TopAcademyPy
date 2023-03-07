a = int(input())
b = input()

res = 0

if b == "ярды":
    res = a * 1.0936
elif b == "милли":
    res = a * 0.00062137
elif b == "дюймы":
    res = a * 39.370


print(res)