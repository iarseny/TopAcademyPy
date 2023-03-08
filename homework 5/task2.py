b = lambda x,y: x ** y

number = int(input())
stepen = int(input())

if 0 <= stepen <= 7:
    print(b(number, stepen))