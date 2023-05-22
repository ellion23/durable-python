#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc(k):
    if k == 1:
        return 1
    else:
        return 1/k**2 + calc(k-1)


def main():
    n = int(input("Введите n: "))
    print("Результат Y =", calc(n))
    return 0


if __name__ == "__main__":
    main()

