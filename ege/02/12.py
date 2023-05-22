def summmmm(s):
    sm = 0
    for i in s:
        sm += int(i)
    return sm



s = 12 * '5' + '2'
while '25' in s:
    s = s.replace('25', '9', 1)

while summmmm(s) != 122:
    s += '2'

print(summmmm(s), s.count('2'))