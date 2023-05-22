file = open('INPUT.TXT', 'r')
l = list()
for i in file:
    l.append(i.rstrip())
print(type(l), l)
s = 0
l.pop(0)
for i in l:
    if i == '0':
        s += 1
print(s)


f = open('INPUT.TXT', 'r')
l = f.read().split()
l.pop(0)
L = list()
for i in l:
    L.append(i)
L.reverse()
print(' '.join(L))


# 106
file = open('INPUT.TXT', 'r')
l = list()
s0 = s1 = 0
for i in file:
    l.append(int(i))
print(l)
l.pop(0)
for i in l:
    if i == 0:
        s0 += 1
    if i == 1:
        s1 += 1
print(min(s0, s1))
print('s0:{}, s1:{},'.format(s0, s1), 'answer:', min(s0, s1))




f = open('INPUT.TXT', 'r')
l = (f.read().split())
L = list()

a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a:
    print('YES')
else:
    print('NO')

for i in l:
    if i + l.index(i+1) == l.index(i + 2):
        print('yes')

# Абузы 81
l = []
f = open('INPUT.TXT', 'r')
for i in f.read().split():
    l.append(int(i))
l.pop(0)
print(min(l), max(l))

# Автобусная экскурсия 233
l, p = [], 0
f = open('INPUT.TXT', 'r')
for i in f.read().split():
    l.append(int(i))
l.pop(0)
for i in l:
    if i <=  437:
        p = l.index(i) + 1
        break
if p == 0:
    print('No crash')
else:
    print('Crash', p)

# sheet - 3 947
a = float(input())
n, s = 2, float()
while a > s:
    s += 1/n
    n += 1
print(n - 2, 'card(s)')
