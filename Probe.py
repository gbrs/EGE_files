txt = ''
with open('ahmadulina.txt', encoding='utf-8') as f:
    for line in f:
        txt += line.strip() + ' '
print(txt.split())
