lst = []
with open('27-B.txt') as f:
    for line in f:
        lst.append(line.strip().split())
lst = lst[1:]
print(lst[-10:-1])
