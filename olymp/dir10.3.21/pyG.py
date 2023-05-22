f = open('input.txt')
l, l2 = [], []
for i in f.readlines():
    l.append(i)
l.pop(-1)
for k in l:
     l2.append(k.split())
l = []
for i in l2:
    if int(i[0])**2 + int(i[1])**2 == int(i[2])**2 or int(i[0])**2 + int(i[2])**2 == int(i[1])**2 or int(i[1])**2 + int(i[2])**2 == int(i[0])**2:
        l.append('right')
    else:
        l.append('wrong')
for i in l:
    print(i)