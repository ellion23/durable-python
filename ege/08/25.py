l = []
for i in range(3614033, 3614117):
    d = 0
    for g in range(2, i // 2 + 1):
        if i % g == 0:
            d += 1
            break
    if d == 0:
        l.append(str(i))

x = 1
for i in l:
    print(x, i)
    x += 1