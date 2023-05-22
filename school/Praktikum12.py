import math
from random import random
n = 10**6
m = 0
for i in range(n):
    x = random()
    y = random()
    if x*x + y*y <= 1:
        m += 1

pi = 4*m/n
print('Pi= ', pi)
error = abs(math.pi - pi) / math.pi * 100
print('Ошибка: ', str(error)[:10])
r = 5
print(pi * r**2)
v = 4 / 3  * pi * r**3
print(v)
