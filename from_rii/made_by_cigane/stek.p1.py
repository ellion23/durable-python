fi = open('input1.txt', encoding='utf8')
l9, l10, l11 = [], [], []

for i in fi:
    class_no, name = i.split()
    if i.split()[0] == '9':
        l9.append(i.split()[1])
    if i.split()[0] == '10':
        l10.append((i.split()[1]))
    if i.split()[0] == '11':
        l11.append(i.split()[1])

for i in l9: print('9', i)
for i in l10: print('10', i)
for i in l11: print('11', i)
