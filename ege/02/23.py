# + 1
# * 2
# 4 to 23
def f(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1
    elif n > 4 and n % 2 == 0:
        return f(n-1) + f(n//2)
    elif n > 4 and n % 2 != 0:
        return f(n-1)


print(f(23))