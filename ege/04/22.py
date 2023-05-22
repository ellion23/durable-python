c = 0
for x in range(1, 10000):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 14 != 0:
            b = b * (x % 14)
        x = x // 14
    if a == 2 and b == 12:
        c += 1
print(c)
