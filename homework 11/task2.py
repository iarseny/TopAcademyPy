spisok = [1, 2, 3, 4, 5, 0, -1,-2, -3, -4, -5]

def pol(s):
    d = 0
    for i in s:
        if i > 0:
            d += 1
    return d

def otr(s):
    d = 0
    for i in s:
        if i < 0:
            d += 1
    return d

def zero(s):
    d = 0
    for i in s:
        if i == 0:
            d += 1
    return d

print(min(spisok), max(spisok), pol(spisok), pol(spisok), otr(spisok), zero(spisok))