# т ь ю р и н г
from itertools import permutations
s = 'тьюринг'
ss = set()
# print(len(set([i  ])))
for i in permutations(s, 6):
    i = ''.join(i)
    if 'ь' != i[0]:
        if 'юь' not in i:
            if 'иь' not in i:
                ss.add(i)
print(len(ss))
# print([i for i in product(s, repeat=6)])