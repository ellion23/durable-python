for x in range(1, 10000):
    xstart = x
    a = 1
    while x > 0:
        a *= x % 7
        x = x // 7
    if a == 54:
        print(xstart, a)
        exit(0)