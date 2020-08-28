txt = 'Надежда Югай'.lower()
print('СРЕЗЫ:')
print(txt[1:7])
print(txt[1:2])
print(txt[0:-1])
print()

print('ШАГИ:')
print(txt[-1:-3:-1])
print(txt[1:7:2])
print(txt[1::2])
print()

print('?:')
print(txt[1:1])
print(txt[-1:-3])
print(txt[20:30])  # слайс не кидает ошибку при выходе за границы списка
                    # или строки, выводя "пустоту"

print('НЕДОМОЛВКИ:')
print(txt[3:])
print(txt[-5:])
print(txt[:6:2])
print(txt[-1::-1])

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('СРЕЗЫ:')
print(lst[1:7])
print(lst[1:2])
print(lst[0:-1])

print('ШАГИ:')
print(lst[-1:-3:-1])
print(lst[1:7:2])
print(lst[1::2])

print('?:')
print(lst[1:1])
print(lst[-1:-3])
print(lst[20:30])  # слайс не кидает ошибку при выходе за границы списка
                    # или строки, выводя "пустоту"

print('НЕДОМОЛВКИ:')
print(lst[3:])
print(lst[-5:])
print(lst[:6:2])
print(lst[-1::-1])

print('минимум:', min(lst[-1::-3]))

for i in lst[2::3]:
    print(i, end=' ')
print()

lst_copy = lst[:]
print(lst_copy)

lst_copy_reversed = lst[::-1]
print(lst_copy_reversed)
