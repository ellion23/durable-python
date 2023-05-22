def f(n):
    if n <= 18:
        return 3 * f(n+1) + n + 8
    elif n > 18:
        return n

print(f(9))