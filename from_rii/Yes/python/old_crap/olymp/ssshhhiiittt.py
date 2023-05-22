from collections import defaultdict
from math import inf


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.min_times = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value == 1:
            self.min_times = 0
        else:
            self.min_times[value] = 1
    def set_min_times(self, node, sced):
        if self.min_times[node] > sced:
            self.min_times[node] = sced

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra_dva(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

def dijkstra(n, s, matrix):
    valid = [True]*n
    weight = [1000000]*n
    weight[s] = 0
    for i in range(n):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(n):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight

g = Graph()
f = open('dickstra.txt', 'r')
n, e = map(int, f.readline().split())
for i in range(n+1):
    g.add_node(i+1)
m = int(f.readline())
for i in range(m):
    l = (list(map(int, f.readline().split())))
    for j in range(1, l[0]):
        if g[j] == 1:
            g.set_min_times(l[2 * j - 1], l[2 * j])
            g.add_edge(l[2 * j - 1], l[2 * j + 1], l[2 * j + 2] - l[2 * j])
        else:
            if g.min_times[l[2 * j - 1]] <= l[2 * j]:
                g.add_edge(l[2 * j - 1], l[2 * j + 1], l[2 * j + 2] - l[2 * j] + l[2 * j] - g.min_times[l[2 * j - 1]])

print(g.nodes)
print(g.edges)
print(g.distances)

visited, path = dijkstra_dva(g, 1)
if visited[e] != inf:
    print(visited[e])
else:
    print(-1)
