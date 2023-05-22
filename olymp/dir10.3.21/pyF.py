import math
f = open('input.txt')
l, l2 = [], []
dy, dx, numr, denr = 0, 0, 0, 0
for i in map(str, f.read().split()):
    l.append(i)
l.pop(0)
for i in l:
    if '(' in i in i:
        p1 = i[0:i.index('.')]
        p2 = i[i.index('.')+1:i.index('(')]
        p3 = i[i.index('(')+1:i.index(')')]
        dy = '9'*len(p3)
        if p2 != '':
            dx = '0'*len(p2)
            numr = int(p2 + p3) - int(p2)
        else:
            dx = ''
            numr = int(p2 + p3)
        denr = int(dy + dx)
        gcd = math.gcd(numr, denr)
        denr //= gcd
        numr //= gcd
        l2.append('{}/{}'.format(numr, denr))
    else:
        p2 = i[i.index('.') + 1:]
        gcd = math.gcd(int(p2), int(10*len(p2)))
        l2.append('{}/{}'.format(int(p2)//gcd, int(10*len(p2))//gcd))
for i in l2:
    print(i)