# Кубик, грани которого помечены цифрами от 1 до 6, бросают N раз.
# Найти вероятность того, что сумма выпавших чисел будет равна Q.
# 1, 3   2, 2
from itertools import product
n, q = 2, 4
states = [1, 2, 3, 4, 5, 6]
num = 0
l = []
for i in product(states, repeat=n):
    if sorted(i) not in l:
        l.append(list(i))
for i in l:
    if true:
        pass