from itertools import product
a = 'mart'
s1 = set([i for i in product(a, repeat=5) if i[0] != i[1] and i[1] != i[2] and i[2] != i[3] and i[3] != i[4]])

print(len(s1))
