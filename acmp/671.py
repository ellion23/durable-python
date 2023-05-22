from itertools import permutations
# n = int(input())
n = 56
l = []
for i in range(1, len(str(n))+1):
    k = [g for g in permutations('47', i)]
    l.append(k)
print(l)
