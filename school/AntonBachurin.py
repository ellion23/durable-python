from random import randint, uniform

# 1
n = int(input('Введите количество значений в массиве: '))
s, l = 0, []
for i in range(n):
    l.append(randint(1000, 2000))
for i in l:
    num = i % 100 // 10
    if num % 2 == 0 and num != 0:
        s += 1
print(s)

# 2
l = [i for i in range(-50, 50, 16)]
print(*l, sep=';')
pr, prpos, su = 1, 1, 0
for i in l:
    pr *= i
    su += i
    if i > 0:
        prpos *= i
print('Произведение: ', pr)
print('Произведение положительныъ: ', prpos)
print('Сумма: ', su)

# 3
l = [i for i in range(150, 200, 3)]
lnew = []
for i in l:
    if i > 180:
        lnew.append(i)
s = sum(lnew) / len(lnew)
print(s)

# 4
n = int(input('Введите количество значений в массиве: '))
l = []
for i in range(n):
    l.append(randint(-2, 2))
s = 0
for i in l:
    if i > 0:
        s += i
print('Сумма положительных элементов массива=', s)

# 5
n = int(input('Введите количество значений в массиве: '))
l = []
for i in range(n):
    l.append(randint(2, 10))
s, sno = 0, 0
for i in l:
    if i % 2 == 0:
        s += 1
    else:
        sno += 1
print('Четных:{}, нечетных:{}'.format(s, sno))

# 6
n = int(input('Введите количество значений в массиве: '))
l = []
for i in range(n):
    l.append(randint(1, 100))
sredn1, sredn2 = 0, 0
k1, k2 = 0, 0
for i in l:
    if i < 50:
        k1 += 1
        sredn1 += i
    else:
        k2 += 1
        sredn2 += i
sredn1 //= k1
sredn2 //= k2
print('Среднее до 50: ', sredn1, 'Среднее после 50: ', sredn2)

# 7
mass = [0, 1, 4, -10, 5, 2, 3, 1, 10, 9]
s = 0
mini = mass.index(min(mass))
maxi = mass.index(max(mass))
if mini > maxi:
    mini, maxi = maxi, mini
    mini += 1
else:
    mini += 1
    mass = mass[mini:maxi]
for i in mass:
    s += i
print('Сумма элементов: ', s)

# 8
n = int(input('Колво элементов='))
mass = [0]*n
m2 = []
for i in range(n):
    mass[i] = uniform(-10, 10)
for i in mass:
    if i < 0:
        m2.append(i)
sredn = sum(m2) / len(m2)
print('Среднее арифметическое отрицательных: ', sredn)


# 9
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
for i in range(n):
    mass[i] = randint(1, 100)
print(mass)
for i in range(1, n, 2):
    mass[i] = 0
print(mass)
