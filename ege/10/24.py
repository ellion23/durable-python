txt = open('ege/10/24-2.txt').read()

maxk = 0
k = ''
maxs = ''
for i in txt:
    if i != '0':
        k += i
    else:
        if len(k) > len(maxs):
            maxs = k
        k = ''

print(len(maxs))
