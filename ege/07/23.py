def f(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1
    else:
        return f(n-1) + f(n-2) + f(n-3)


def g(n):
    if n < 8:
        return 0
    elif n == 8:
        return 1
    else:
        return f(n-1) + f(n-2) + f(n-3)


print(f(8) * g(15))