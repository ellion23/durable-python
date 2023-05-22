def dfsodin(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfsthor(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfsthor(graph, start, visited)
    return visited


f = open('bez_raznitsy_kak.txt', 'r')
n, s = map(int, f.readline().split())
g = [set() for i in range(n)]

for i in range(n):
    s1 = list(map(int, f.readline().split()))
    for j in range(n):
        if s1[j] == 1:
            g[i].add(j)
            g[j].add(i)
visited = dfsodin(g, s-1)
print(len(visited))

c = [0 for i in range(n)]
found = True
s = 0
k = 0
while found:
    k += 1
    visited = dfsodin(g, s)
    for i in visited:
        c[i] = k
    s = -1
    for j in range(n):
        if c[j] == 0:
            s = j
            break
    if s == -1:
        break

print(c)