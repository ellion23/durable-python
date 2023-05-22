def dfsodin(graph, start, time):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


f = open('bez_raznitsy_kak.txt', 'r')
n, s = map(int, f.readline().split())
g = [set() for i in range(n)]
time = 1

for i in range(s):
    a, b = list(map(int, f.readline().split()))
    g[a-1].add(b-1)
    g[b-1].add(a-1)

c = [0 for i in range(n)]
found = True
start = 0
print(g)
visited = dfsodin(g, start, time)
print(visited)