start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(i)

print()

for i in range(end + 1, start, -1):
    print(i)

print()

for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)

print()

for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)