k = 0
for s in range(1, 10000):
    n = 1
    while s > n:
        s = s - 15
        n = n * 5
    if n == 125:
        k += 1
print(k)
