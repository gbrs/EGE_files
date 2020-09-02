'''выводим 20 50 80'''
lst = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
for i in range(2, 10, 3):
    print(lst[i], end=' ')
print()

for i in lst[2:10:3]:
    print(i, end=' ')
print()

for i in range(20, 100, 30):
    print(i, end=' ')
print()


'''суммируем все элементы списка'''
s = 0
for i in range(10):
    s += lst[i]
print(s)

s = 0
for i in range(len(lst)):
    s += lst[i]
print(s)

s = 0
for i in lst:
    s += i
print(s)

print(sum(lst))

for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
print()

for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
print()

for i in 'hello world':
    if i == 'a':
        break
    print(i * 2, end='')
else:
    print('\n', 'Буквы a в строке нет', sep='')
