def f(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n > 3 and n % 2 == 0:
        return f(n-1) + f(n-2) + f(n // 2)
    elif n > 3 and n % 2 != 0:
        return f(n-1) + f(n-2) + f(n // 2)


def g(n):
    if n < 10:
        return 0
    elif n == 10:
        return 1
    elif n == 11:
        return 1
    elif n > 11 and n % 2 == 0:
        return g(n-1) + g(n-2) + g(n // 2)
    elif n > 11 and n % 2 != 0:
        return g(n-1) + g(n-2) + g(n // 2)


print(f(10)*g(12))