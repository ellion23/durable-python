l = []
for s in range(1, 1000):
    start = s
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    if n == 210:
        l.append(start)
print(l)