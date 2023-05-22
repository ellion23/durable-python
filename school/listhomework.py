from random import randint, uniform

# 1
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
summ = 0
for i in range(n):
    mass[i] = randint(1000, 2000)
for i in mass:
    num = i % 100 // 10
    if num % 2 == 0 and num != 0:
        summ += 1
print(summ)

# 2
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
for i in range(n):
    mass[i] = randint(-20, 20)
pr1, pr2, su = 1, 1, 0
for i in mass:
    pr1 *= i
    su += i
    if i > 0:
        pr2 *= i
print('Произведение элементов массива: ', pr1)
print('Произведение положительных элементов массива: ', pr2)
print('Сумма ненулевых элементов массива: ', su)

# 3
mass = [i for i in range(150, 200, 3)]
sredn, k = 0, 0
for i in mass:
    if i > 180:
        k += 1
        sredn += i
sredn //= k
print(sredn)

# 4
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
for i in range(n):
    mass[i] = randint(-2, 2)
s = 0
for i in mass:
    if i > 0:
        s += i
print('Сумма положительных элементов массива=', s)

# 5
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
for i in range(n):
    mass[i] = randint(2, 10)
schetn, snechetn = 0, 0
for i in mass:
    if i % 2 == 0:
        schetn += 1
    else:
        snechetn += 1
print('Четных:{}, нечетных:{}'.format(schetn, snechetn))

# 6
n = int(input('Введите количество значений в массиве: '))
mass = [0]*n
for i in range(n):
    mass[i] = randint(1, 100)
sredn1, sredn2 = 0, 0
k1, k2 = 0, 0
for i in mass:
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
