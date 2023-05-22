# F(n) = 2·n – 5 при n > 12
# F(n) = 2·F(n+2) + n – 4, если n ≤ 12
def f(n):
    if n <= 12:
        return 2*f(n+2) + n - 4
    elif n > 12:
        return 2*n - 5


print(f(1))
