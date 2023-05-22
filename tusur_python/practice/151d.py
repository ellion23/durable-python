#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import factorial


def calc(x, k):
    a, y = 1, 1
    i = 2
    while a > k:
        a = x**i / factorial(i)
        y += a
        i *= 2
    return y


def main():
    x, k = map(float, input("Введите x и точность: ").split())
    print("Результат y =", calc(x, k))
    return 0


if __name__ == "__main__":
    main()