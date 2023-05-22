# 8
from itertools import product
a = '01234'
# s1 = set([i for i in product(a, repeat=5) if ((i.count('2') + i.count('4') + i.count('0')) <= 3) and i[0] != '0'])
s1 = set()
for i in product(a, repeat=5):
    if ((i.count('2') + i.count('4') + i.count('0')) <= 3) and i[0] != '0':
        s1.add(i)
print(len(s1))
