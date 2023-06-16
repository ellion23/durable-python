#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import factorial, prod


def calc_144a(k):
    if k == 1:
        return 1
    else:
        return 1/k**2 + calc_144a(k-1)


def ex144a():
    n = int(input("1.4.4a\nВведите n: "))
    print("Результат Y =", calc_144a(n), '\n')


def calc_151d(x, k):
    a, y = 1, 1
    i = 2
    while a > k:
        a = x**i / factorial(i)
        y += a
        i *= 2
    return y


def ex151d():
    x, k = map(float, input("1.5.1д\nВведите x и точность: ").split())
    print("Результат y =", calc_151d(x, k), '\n')


def ex151i():
    x, k = map(float, input("1.5.1и\nВведите x и точность: ").split())
    while abs(x) > 1:
        print("|x| должен быть <= 1")
        x = float(input("Введите x: "))

    i = 1
    y0 = x
    y = x
    sign = 1
    while y0 > k:
        i += 2
        sign *= -1
        numerator = [i for i in range(1, i, 2)]
        denominator = [i for i in range(2, i + 1, 2)]
        y0 = sign * (prod(numerator) / prod(denominator)) * (x ** i / i)
        y += y0

    print("Результат y =", y, '\n')


def main():
    # ex144a()
    # ex151d()
    ex151i()
    return 0


if __name__ == "__main__":
    main()
