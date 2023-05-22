def f(n):
    b = str(n)
    l = sorted([int(b[0])**2 + int(b[1])**2, int(b[1])**2 + int(b[2])**2])
    g = int(str(l[1])+str(l[0]))
    return g


for i in range(1000, 300, -1):
    if f(i) == 9752:
        print(i, f(i))
        exit(0)


