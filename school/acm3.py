f = open('INPUT.TXT')
l, p, d = [], [], 0
for i in f.read().split():
    l.append(int(i))
for i in range(3):
    p.append(l[-1])
    l.pop(-1)
for i in range(3):
    d += max(l) * max(p)
    l.pop(l.index(max(l)))
    p.pop(p.index(max(p)))
print(d)
