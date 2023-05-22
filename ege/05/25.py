l = []
for g in range(1532040, 1532160):
    x = 1
    for i in range(2, g//2+1):
        if g % i == 0:
            x += 1
    if x == 1:
        l.append(g)
l = l[::-1]
for h in l:
    print(h)
