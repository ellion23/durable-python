import math
k = 1
l = []

for i in range(194441, 196501):
    for d in range(1, i//2 + 1):
        if i % d == 0:
            k += 1
    if k % 2 == 0:
        k = 1
    else:
        l.append(i)
        k = 1


for i in l:
    print(i, math.sqrt(i))