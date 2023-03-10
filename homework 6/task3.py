start = int(input())
end = int(input())

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)