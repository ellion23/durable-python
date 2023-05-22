def f(n):
    b = bin(n)[2:]
    for i in range(2):
        if b.count('1') % 2 == 1:
            b += '1'
        else:
            b += '0'
    return int(b, 2)


x = 0
while f(x) <= 43:
    x += 1
print(x, f(x))
