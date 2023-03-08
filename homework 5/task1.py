number = int(input())

if number > 100 or number < 1:
    print("Not diaposone")
elif number % 3 == 0 and number % 5 != 0:
    print("Fizz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 != 0:
    print("Fizz Buzz")
elif number % 3 != 0 and number % 5 != 0:
    print(number)