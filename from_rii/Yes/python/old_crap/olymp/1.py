def printmatrix(m):
    r,c = len(m),len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()

f = open('inpat.txt', 'r')

n = int(f.readline())
graphs = list(map(int, f.readline().split()))

# take input values
for i in range(n):
    graphs[0][1] = graphs[2]

printmatrix(graphs)
print("-------------------")
# apply our algo
# T.C = O(v^3)
for k in range(n):
    for i in range(n):
        for j in range(n):
            # cost of tmp path is less
            # update
            if graphs[i][k]+graphs[k][j] < graphs[i][j]:
                graphs[i][j] = graphs[i][k] + graphs[k][j]

printmatrix(graphs)