'''
# 1
l = list()
for i in range(10000, 100000):
    if i % 133 == 125 and i % 134 == 111:
        l.append(i)
print('Числа: ', l)

# 2
l = list()
s = 1
n = int(input('Введите n: '))
for i in range(1, n + 1):
    s += (1 / i**2)
    l.append(1 / i**2)
print('Сумма чисел: ', s, 'Числа: ', l)

# 3
s = k = 0
n = int(input('Введите n: '))
for i in range(1, n + 1):
    if i % 5 == 0 and i % 7 != 0:
        s += i
        k += 1
print('Сумма чисел: {}, Кол-во чисел: {}'.format(s, k))

# 4
l = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
for i in range(7):
    if i < 5:
        print('{}-й день недели - {}, рабочий день'.format(i+1, l[i]))
    if i > 4:
        print('{}-й день недели - {}, выходной день'.format(i+1, l[i]))

# 5
n = int(input('Введите n для вычисления кубов: '))
for i in range(1, n + 1):
    print('{}^3 = {}'.format(i, i**3))

# 6
l = []
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        l.append(i)
print(l)
'''
# 7
n1, n2 = map(int, input('Введите границы промежутка: ').split())
k = 0
l = []
for i in range(n1, n2 + 1):
    if (i % 9 == 0 or i % 23 == 0) and i % 13 != 0 and i % 18 != 0 and i % 19 != 0 and i % 22 != 0:
        k += 1
        l.append(i)
print(k, max(l))

# 8
n1, n2 = map(int, input('Введите границы промежутка: ').split())
k = 0
l = []
for i in range(n1, n2 + 1):
    if i % 9 == 0 and i % 15 == 0 and i % 6 != 0 and i % 12 != 0 and i % 17 != 0 and i % 21 != 0:
        k += 1
        l.append(i)
print(k, min(l))
