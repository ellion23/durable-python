for d in range(1, 10000):
    dst = d
    n = 2
    s = 0
    while s <= 365:
        s = s + d
        n = n + 5
    if n == 67:
        print(dst)