
def floyd(a):
    v = range(len(a))
    for k in v:
        for i in v:
            for d in v:
                a[i][d] = min(a[i][d], a[i][k] + a[k][d])

    for m in v:
        if a[m][m] < 0: # negative cycle found
            return -1
    return 0


f = open('inpat.txt', 'r')
n = int(f.readline())

graphs = list()

for i in range(n):
    graphs.append(list(map(int, f.readline().split())))
print(graphs)
floyd(graphs)
print(graphs)
