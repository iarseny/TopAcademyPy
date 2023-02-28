def calculator(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        return number1 / number2

a = input()
b = input()
s = input()
print(calculator(int(a),int(b),s))