for s in range(10000, 1, -1):
    st = s
    n = 0
    while s >= 4:
        s = s - 4
        n = n + s - s % 4
    if n == 84:
        print(st)
        exit(0)