from collections import deque

l = deque()
f = open('input2.txt')
s = f.read()
c = 0


for k in s:
    if k == '{' or k == '(' or k == '[':
        c += 1
    if k == '}' or k == ')' or k == ']':
        c -= 1

if c == 0:
    for i in s:
        if i == '{' or i == '(' or i == '[':
            l.append(i)
        if i == '}':
            if '{' in l:
                l.remove('{')
        if i == ')':
            if '(' in l:
                l.remove('(')
        if i == ']':
            if '[' in l:
                l.remove('[')
else:
    print('no')


if l == deque():
    print('yes')
else:
    print('no')
