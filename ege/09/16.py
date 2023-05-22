def f(n):
    if n == 0:
        return 3
    elif n < 0:
        return 0
    elif n <= 15:
        return f(n-1)
    elif n > 15 and n < 100:
        return 2.5 * f(n-3)
    elif n >= 100:
        return 3.3 * f(n-2)


print(f(100))