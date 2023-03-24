from not_for_checking import make_list

s = []

a = make_list()
b = make_list()

for i in a:
    g = True
    for j in b:
        if i == j:
            g = False

    if g:
        s.append(i)

for i in b:
    g = True
    for j in a:
        if i == j:
            g = False

    if g:
        s.append(i)

print(s)