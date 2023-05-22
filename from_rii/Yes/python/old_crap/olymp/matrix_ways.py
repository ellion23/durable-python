import collections
f = open('inpat.txt', 'r')
n = int(f.readline())
l = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    l[i] = list(map(int, f.readline().split()))
s = [set() for i in range(n)]
graph = dict()
for i in range(0, n):
    for j in range(i, n):
        if l[i][j] != 0:
            s[i].add(j)
            s[j].add(i)
            graph[i] = j
            graph[j] = i

step = 0  ##Steps of searching (input into!)
comp = 0  ##If search complete, then 1
white_list = {}  ##Clear graphs
gray_list = {}  ##Searched
black_list = {}  ##Dead ends
queue = {}
print(graph)
def bfs(graph, root):
    seen = set([root])
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        #visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
#               dist[node] = dist[vertex] + 1
if __name__ == '__main__':
    bfs(graph, 0)