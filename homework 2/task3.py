mil = lambda x: x * 1000
sm = lambda x: x * 100
d = lambda x: x * 10
m = lambda x: x * 0.00062

x = int(input())

print(str(mil(x)) + " " + str(sm(x)) + " " + str(d(x)) + " " + str(m(x)))