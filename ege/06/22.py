xmax = 0
for x in range(1, 100000):
    xstart = x
    L = 0
    M = 0
    while x > 0:
      L = L + 1
      if x % 2 == 0:
        M = M + (x % 10)
      x = x // 10
    if L == 3 and M == 0:
        if xmax < xstart:
            xmax = xstart
print(xmax)