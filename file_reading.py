'''текст в одну строчку'''
with open('text_row.txt') as f:
    txt = f.read()
print(txt[-10:])


'''текст из нескольких строчек 
превращаем в одну строчку'''
txt = ''
with open('text_rows_rus.txt') as f:
    for line in f:
        txt += line.strip()
print(txt)
txt = txt[1:]
print(txt)


'''чтение чисел, идущих через запятую, из строки'''
with open('numbers_row') as f:
    lst = f.read().strip().split(',')
    lst = list(map(int, lst))
print(lst[-5:])


'''чтение чисел, каждое из которых в своей строке'''
lst = []
with open('numbers_column.txt') as f:
    for line in f:
        lst.append(line.strip())
lst = lst[2:]
lst = list(map(int, lst))
print(lst[-5:])


'''чтение пар чисел, каждая из которых в своей строке'''
lst = []
with open('numbers_columns_small.txt') as f:
    for line in f:
        pair = line.strip().split()
        pair = list(map(int, pair))
        lst.append(pair)
lst = lst[1:]
print(lst[-3:])
