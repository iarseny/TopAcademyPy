from math import sqrt

def number_is_prost(number):
    n = 0
    for i in range(1, number + 1):
        if number % i == 0:
            n += 1
    return n == 2

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if number_is_prost(i):
        print(i)