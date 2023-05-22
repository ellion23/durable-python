def f(n):
    b = bin(n)[2:]
    return int(b[::-1], 2)


for i in range(100, 1, -1):
    if f(i) == 9:
        print(f(i), i)
        exit(0)