def f(n):
    if n == 3:
        return 1
    elif n < 3:
        return 0
    elif n > 3:
        return f(n - 1) + f(n - 2) + n-1


print(f(10))
