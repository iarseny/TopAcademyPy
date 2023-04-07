while True:
    a, b = int(input()), int(input())
    number = int(input())

    if number in range(a, b + 1):
        for i in range(a, b + 1):
            if i == number:
                print("!" + str(i) + "! ", end="")
            else:
                print(str(i) + " ", end="")
        break
