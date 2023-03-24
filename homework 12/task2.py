s = []
from not_for_checking import make_list

a = make_list()
b = make_list()

for i in a:
    s.append(i)

for i in b:
    if i not in s:
        s.append(i)

print(s)