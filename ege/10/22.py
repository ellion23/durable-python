for x in range(1, 10000):
    xs = x
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += 9 - x % 10
        x //= 10
    if a == 2 and b == 8:
        print(xs)
        exit(0)
