def f(n):
    bn = bin(n)[2:]
    if n < 4:
        return 0
    elif n == 4:
        return 1
    elif n > 4 and bn[0] != '1':
        return f(n-1)
    else:
        return f(n-1) + f(int(bn[1:], 2))


print(f(49))