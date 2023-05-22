import math

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
