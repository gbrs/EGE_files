lst = [2, 6, 10, 5, 4, 2]
string = 'vsdab'

# статистика
print(max(lst))
print(min(string))
print(sum(lst))

# математика
print(abs(-12.96))
print(int(12.5))
print(round(12.5))
# упс
print(hex(42))
print(oct(42))
print(bin(42))
# сколько чисел в 16-ричной записи числа 548787431486762145?
print(len(str(hex(548787431486762145))) - 2)
print('36-ричное число zd3s84 в десятеричной системе:', int('zd3s84', 36))
print()

print(string)
print(sorted(string))
print(string)
lst_str = sorted(string)
lst_str = list(reversed(lst_str))
print(lst_str)
print()

help([].pop)
print(dir(str))
print(dir(list))
