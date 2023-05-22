count, minnum = 0, 10000000
for i in range(20789, 35673):
    d = 1
    for g in range(1, i//2+1):
        if i % g == 0:
            d += 1
    if d == 5:
        count += 1
        if minnum > i:
            minnum = i
print(count, minnum)
