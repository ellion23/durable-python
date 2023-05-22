import math


# Задание 4
a, b, c = map(float, input('Введите 3 числа ч. п. = ').split())
print(a < (b + c) and b < (a + c) and c < (a + b))

# Задание 5
# Если x и y равны 12 и 35, то ответ -0.01
x, z = map(int, input('Введите целые числа ч. п. x и y = ').split())
c = (x + 20 - z + 5) / (15 * (15 - z))
print('Результат каких-то вычислений: {:.2f}'.format(c))

# Домашняя работа 5.1
x = int(input('Введите четырехзначное число x = '))  # x = 1221
a = x // 1000
b = x // 100 % 10
c = x % 100 // 10
d = x % 10
print('Равна ли сумма первых двух и последних цифр числа {} ->'.format(x),
      (a + b) == (c + d))

# Матан
x = -12.56
print('x = -12.56')
print('Число Пи = {}'.format(math.pi))
print('Модуль числа x = {}'.format(abs(x)))
print('Преобразованное к целому числу x = {}'.format(int(x)))
print('Округление x = {}'.format(round(x)))
print('Квадратный корень от модуля x = {}'.format(math.sqrt(abs(x))))
print('Экспонента x = {}'.format(math.exp(x)))

# Задание 6
r = int(input('Введите радиус окружности r = '))
L = 2 * math.pi * r
S = math.pi * r ** 2
print('Длина окружности = {:.3f} \nПлощадь окружности = {:.3f}'.format(L, S))

# Задание 7
a, b, c = map(int, input('Введите стороны треугольника a, b и c = ').split())
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
r = S / p
R = (a * b * c) / (4 * S)
print('S = {}, r = {}, R = {}'.format(S, r, R))

# Задание 8
a, b, C = map(int, input('Введите стороны a, b и угол C = ').split())
C *= math.pi / 180
S = 0.5 * a * b * math.sin(C)
print('Площадь треугольника S = {:.1f}'.format(S))
