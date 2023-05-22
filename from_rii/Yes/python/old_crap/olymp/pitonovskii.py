import collections

def bfs(graph: list, root: int, dist: list):
    seen = set([root])
    dist[root] = 0
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        #if vertex == f:
        #    break
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
                dist[node] = dist[vertex] + 1

f = open('bez_raznitsy_kak.txt', 'r')
n = int(f.readline())
l = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    l[i] = list(map(int, f.readline().split()))

s = [set() for i in range(n)]

for i in range(0, n):
    for j in range(i, n):
        if l[i][j] != 0:
            s[i].add(j)
            s[j].add(i)
start, finish = map(int, f.readline().split())
d = [-1 for i in range(n)]
bfs(s, start-1, d)
#print(d[finish-1])

path = [0 for i in range(d[finish-1]+1)]

vertex = finish-1
for i in range(d[finish-1], -1, -1):
    for j in range(s[vertex]):
        if d[j] == i-1:
            path[i] = j+1
            vertex = j
    a = d.index(i)
    path[i] = (a+1)
path = reversed(path)
print(*path)
