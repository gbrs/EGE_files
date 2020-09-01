'''чтение чисел, каждое из которых в своей строке'''
lst = []
with open('numbers_column.txt') as f:
    # или просто lst = f.read().strip().split()
    # for line in f:
    #     lst.append(line.strip())
    a, b = f.readline().split()
    for line in f:
        lst.append(int(line.strip()))
print(lst[:5])
lst = lst[1:]
lst = list(map(int, lst))
print(lst[:4])
