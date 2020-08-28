lst1 = [0, 2, 4, 6, 8]
lst2 = [1, 3, 5, 7, 9]
lst3 = [5, 8, 2, 5, 4, 3, 2, 9, 5, 8]

print(sum(lst1))
print()

print('обращение к элементам:')
print(lst1[-2])
print(lst1[-1:1:-1])

print('конкатенация:')
lst12 = lst1 + lst2
print(lst12)
print()

print('методы списков:'.upper())
print()

print('добавление:')
lst12.extend(lst1)
print(lst12)
print(lst1)
lst1.append(10)  # return = None
print(lst1)

print('удаление:')
lst1.pop(0)  # возвращает попнутое число
print(lst1)
lst1.pop()
print(lst1)
lst1.remove(4)
print(lst1)
print('вставка на позицию 1:')
lst1.insert(1, 'вставка')
print(lst1)
print('замена на позиции 1:')
lst1[1] = 'замена'
print(lst1)
print()

print('первая позиция двойки в lst3:')
print(lst3)
print(lst3.index(2))
print('число вхождений пятёрки в список lst3:')
print(lst3)
print(lst3.count(5))
print()

print('сортировка:')
lst3.sort()
print(lst3)
print('реверс:')
lst3.reverse()
print(lst3)
print('и обратно срезом:')
lst3 = lst3[::-1]
print(lst3)
print()

print('есть ли в списке lst3 девятка?')
print(9 in lst3)
print()

string3 = '13579'
print('преобразование строки в список:')
list3 = list(string3)
print(list3)
list3 = list(map(int, string3))
print(list3)

string5 = 'раз два три четыре пять раз два'
print('преобразование строки в список слов:')
list5 = list(string5.split())
print(list5)
print('множество (элементы не повторяются):')
set5 = set(list5)
print(set5)
