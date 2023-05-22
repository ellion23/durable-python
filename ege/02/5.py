def f(n):
    st = str(n)
    l = []
    l.append(int(st[0]) + int(st[2]) + int(st[4]))
    l.append(int(st[1]) + int(st[3]))
    l.sort()
    s = ''
    for k in l:
        s += str(k)
    return s


for x in range(10000, (10**5) + 1):
    if f(x) == '621':
        print(x)