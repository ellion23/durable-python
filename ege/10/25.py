l = []
n = 860000
while True:
    n += 1
    d = 0
    m = 0
    maxd, mind = 0, 10**12
    for g in range(2, n // 2 + 1):
        if n % g == 0:
            d += 1
            mind = min(mind, g)
            maxd = max(maxd, g)
    if d >= 2:
        m = maxd-mind
        if m % 100 == 18:
            l.append([n, m])
    if len(l) == 5:
        for dd in l:
            print(*dd)
        exit(0)