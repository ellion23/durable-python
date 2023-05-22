f = open('bez_raznitsy_kak.txt', 'r')
res = list()
m = list()
am, lu = map(int, f.readline().split())
res = [[0 for i in range(am)] for j in range(am)]
print(am, lu)

for a in range(am):
    m.append(list(map(int, f.readline().split())))

