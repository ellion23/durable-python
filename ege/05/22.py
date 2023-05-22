for x in range(1, 10000):
    xstart = x
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0:
            a = a + 1
        else:
            b = b + 1
        x = x // 8
    if a == 3 and b == 2:
        print(xstart)