z = 1
l = []
for g in range(5336748, 5336835):
    x = 0
    for i in range(2, g//2+1):
        if g % i == 0:
            x += 1
    if x == 0:
        l.append(g)
for h in l:
    print(z, h)
    z += 1
