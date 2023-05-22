def f(n):
    if n == 2:
        return 1
    elif n < 2:
        return 0
    elif n > 2:
        return f(n - 1) + f(n - 3)


def g(n):
    if n == 10:
        return 1
    elif n == 15:
        return 0
    elif n < 10:
        return 0
    elif n > 10:
        return f(n - 1) + f(n - 3)


print(f(9) + g(20))
