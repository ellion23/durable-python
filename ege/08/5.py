def f(n):
    b = bin(n)[2:]
    b += b[-2]
    b += b[1]
    return int(b, 2)


x = 2
while f(x) <= 210:
    x += 1
print(x, f(x))
print(x-1, f(x-1))
