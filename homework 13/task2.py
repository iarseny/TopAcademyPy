string = input()
numbers = 0
words = 0
for i in string:
    if i.isdigit():
        numbers += 1
    else:
        words += 1

print(numbers, words)