def fu(n):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    return int(b, 2)


for g in range(1, 1000):
    if fu(g) > 170:
        print(g, fu(g))