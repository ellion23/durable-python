def f(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return f(n-1) + f(n-2)


def g(n):
    if n < 7:
        return 0
    elif n == 7:
        return 1
    elif n > 7:
        return f(n - 1) + f(n - 2)


print(f(6) + g(12))
