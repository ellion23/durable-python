# 25
numerals = dict()
for i in range(586132, 586431):
    d = 2
    maxd = 0
    for g in range(2, i//2+1):
        if i % g == 0:
            d += 1
            maxd = max(maxd, g)
    if d > 72:
        numerals[i] = d, g
print(numerals)
