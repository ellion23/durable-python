f = open('inpoot.txt', 'r')
k = int(f.readline())
for d in range(k):
    n = int(f.readline())
    flies = []
    for i in range(n):
        flies.append(list(map(int, f.readline().split())))
    m = int(f.readline())
    beat = []
