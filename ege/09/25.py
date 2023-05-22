c = 0
l = []
for i in range(248015, 251577, 2):
    d = 2
    gm = 0
    for g in range(2, i // 2 + 1):
        if i % g == 0:
            d += 1
            gm = g
    if d % 2 != 0:
        l.append([i, gm])
        gm = 0

for i in l:
    print(i)
# [249001, 499]
# [251001, 83667]
