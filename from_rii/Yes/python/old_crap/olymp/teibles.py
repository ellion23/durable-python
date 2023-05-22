def dfsodin(graph, start, colors):
    visited, stack = set(), [start]
    color = 1
    error = False
    while stack:
        vertex = stack.pop()
        if colors[vertex] != 0 and colors[vertex] != color:
            error = True
            break
        if ((colors[vertex] == 0) or (colors[vertex] == color)) and (vertex not in visited):
            visited.add(vertex)
            colors[vertex] = color
            if color == 1:
                color = 2
            else:
                color = 1
                stack.extend(graph[vertex] - visited)
    return visited, error


f = open('bez_raznitsy_kak.txt', 'r')
n, s = map(int, f.readline().split())
g = [set() for i in range(n)]

for i in range(s):
    a, b = list(map(int, f.readline().split()))
    g[a-1].add(b-1)
    g[b-1].add(a-1)

c = [0 for i in range(n)]
found = True
start = 0
while found:
    visited, r = dfsodin(g, start, c)
    if r == True:
        print('NO')
        break
    elif r == False:
        print('YES')
        break
for i in c:
    if i != 0:
        print(i, end = ' ')