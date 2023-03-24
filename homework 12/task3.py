from not_for_checking import make_list

s = []
a = make_list()
b = make_list()

for i in a:
    for j in b:
        if i == j:
            s.append(i)

print(s)