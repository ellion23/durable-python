def f(n):
    b = bin(n)[2:]
    b += b[-2]
    b += b[1]
    return int(b, 2)


n = 2
while f(n) <= 100:
    n += 1

print(f(n), n)
print(f(n-1), n-1)
