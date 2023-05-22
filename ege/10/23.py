def f(n):
    if n == 5:
        return 1
    elif n < 5:
        return 0
    elif n > 5:
        return f(n-2) + f(n-7)


print(f(49))