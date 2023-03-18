all_numbers = []

while True:
    tmp = int(input())
    if tmp != 7:
        all_numbers.append(tmp)
    else:
        print("Good bye!")
        break

print(sum(all_numbers), max(all_numbers), min(all_numbers))