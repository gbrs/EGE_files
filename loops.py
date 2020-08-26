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


s = 0
for i in range(10):
    s += lst[i]
print(s)

s = 0
for i in lst:
    s += i
print(s)

print(sum(lst))
