def f(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    elif n == 10:
        return 0
    elif n > 3:
        return f(n-1) + f(n-3)


def g(n):
    if n < 15:
        return 0
    elif n == 15:
        return 1
    elif n > 15:
        return f(n-1) + f(n-3)


print(f(14) * g(20))
