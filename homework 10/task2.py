string = input()
go = int(input("Введите размер списка: "))
spisok = []

for i in range(go):
    spisok.append(input())


for i in spisok:
    string = string.replace(i, i.upper())

print(string)