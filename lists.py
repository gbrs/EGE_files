lst1 = [0, 2, 4, 6, 8]
lst2 = [1, 3, 5, 7, 9]
lst3 = [5, 8, 2, 5, 4, 3, 2, 9, 5, 8]

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
print('число вхождений пятёрки в список lst3:')
print(lst3)
print(lst3.count(5))
print('сортировка:')
lst3.sort()
print(lst3)
lst3.reverse()
print(lst3)

print()

string3 = '13579'
print('преобразование строки в список:')
list3 = list(string3)
print(list3)
list3 = list(map(int, string3))
print(list3)
