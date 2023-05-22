for s in range(1, 1000):
    st = s
    n = 2
    while s < 45:
        s = s + 3
        n = n * 2
    if n == 128:
        print(st, n)
        break
