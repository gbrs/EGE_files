string1 = ' абраКАДАБРА'
string2 = 'АБРАкадабра '
string3 = '13579'
string4 = '02468'

print('конкатенация:')
print(string1 + string2)
print(string3 + string4)
print('-=-'.join([string1, string3, string2, string4]))

print()
print('методы строк:')
print(string1)
print(string1.strip())
print(string1.lower() + '<->' + string2.upper())
print(string1.strip().lower() + '<->' + string2.strip().upper())
string5 = 'торторт, вкусный торт.'
print(string5)
print('количество непересекающихся совпадений для слова торт:')
print(string5.count('торт'))
print('замена торт на ТАРТ и удаление знаков препинания:')
string5 = string5.replace('торт', 'ТАРТ')  # метод делает копию
string5 = string5.replace('.', '')
string5 = string5.replace(',', '')
print(string5)
print()

print('обращение к элементам строк:')
print(string3[2])
print('вывод строки задом наперёд:')
for i in range(len(string4)-1, -1, -1):
    print(string4[i], end='')
print()
print('но срезом проще:')
print(string4[::-1])
print()

print('есть ли в строке string5 вк?')
print('вк' in string5)
print()

string34 = ''
for i in range(5):
    string34 += string4[i] + string3[i]
print(string34)
print()

number = 564687954231548789746513453421655487897987
print('В числе', len(str(number)), 'разряда')
print()

print('преобразование списка в строку:')
lst = [1, 35, 7, 9]
lst = list(map(str, lst))
str_ = ' :-) '.join(lst)
print(str_)
