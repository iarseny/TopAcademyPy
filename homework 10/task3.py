string = input()
print(len(string.split(".")) - 1 + len(string.split("?")) - 1 + len(string.split("!")) - 1)