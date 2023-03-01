a = input("Сообщение: \n")
n = int(input("Символов: \n"))

print(a[1:])
print(a[n:])
s = a.split(" ")
res = ""
for i in s:
    res += i + "\t"
print(res)

n = int(input())
s[n - 1] = input()

# new_res = ""
# for j in s:
#     new_res += j;

print(" ".join(s))