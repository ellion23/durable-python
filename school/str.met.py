#1
s = input('Введите строку с а и б: ')
s2 = ''
for i in s:
    if i == 'а':
        s2 += 'б'
    elif i == 'А':
        s2 += 'Б'
    elif i == 'б':
        s2 += 'а'
    elif i == 'Б':
        s2 += 'А'
    else:
        s2 += i
print(s2)

#2
s = input('Введите строку для умножения: ')
tmp = 1
for i in s:
    if i == '*':
        continue
    else:
        tmp *= int(i)
print(tmp)

#3
s = input('word -> letter: ')
print(s.replace('word', 'letter'))

#4
s = 'да нет да нет да нет да нет нет'
print(s.replace('да', ''))

#5
s, s2 = 'programming, update, application', ''
for i in s:
    if i == 'a':
        s2 += i + 'b'
    else:
        s2 += i
print(s2)

#6
s = 'Привет, мир!'
print(s[-4:-1])

#7
s = '  Вася не    пошел гулять         грустно           за Васю  '
print(len(s.rsplit(maxsplit=-1)))