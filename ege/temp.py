# (№ 4230) (А. Куканова) Варя составляет пятизначные числа в шестнадцатиричной системе счисления, в которых цифры
# расположены в порядке неубывания. Сколько различных чисел может составить Варя?
# ответ 11628

from itertools import product


def f(word):
    ws = [int(i, 16) for i in word]
    b = True
    for i in range(len(ws)-1):
        if ws[i] <= ws[i-1]:
            pass
        else:
            b = False
    return b


def g(word):
    ws = [i for i in word if i.isdigit()]
    if ws == sorted(ws):
        return True
    else:
        return False


a = '1234567890ABCDEF'
words = set(i for i in product(a, repeat=5) if f(i) and i[0] != 0)
print(len(words))
