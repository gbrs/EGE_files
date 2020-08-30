# number = '8' * 88
# print(number)


# txt = ''
# with open('caroll.txt', encoding='utf-8') as f:
#     for line in f:
#         txt += line.strip() + ' '
# for i in ('.', ',', ';', ':', '—', '?', '!', "'", '-'):
#     txt = txt.replace(i, '')
# print(txt[:100].lower())
# print(list(txt[:100].lower().split()))

def F(n):
    if n > 2:
        return F(n-1) + G(n-2)
    else:
        return 2
def G(n):
    if n > 2:
        return G(n-1) + F(n-2)
    else:
        return 2

print(F(20))
