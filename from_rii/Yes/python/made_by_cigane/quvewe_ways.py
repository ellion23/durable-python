from collections import deque
wall = ('=', '+')
finish = 'F'
start = (1,1)
f = open('queue-maze.txt')
maze = [str(i).rstrip() for i in f.readlines()]
q = deque()


q.append((start, 0))
visited = dict()
while q:
    t, step = q.popleft()
    visited[t] = step
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (maze[t[0]+i][t[1]+j] not in wall) and ((t[0]+i, t[1]+j) not in visited.keys()):
                q.append(((i, j), step + 1))

print(*q)























def BFS(maze, start, goal):

    queue = deque([start])

    visited = set(([start]))

    d = 0

    while(queue):

        x, y = queue.popleft()

        if ((x,y) == goal):
            return x

        if (start != (x,y)):
            maze[x][y] = d

        visited.add((x,y))

        if (maze[x][y+1] not in wall and (x,y+1) not in visited):
            queue.append((x,y+1))

        if (maze[x][y-1] not in wall and (x,y-1) not in visited):
            queue.append((x,y-1))

        if (maze[x-1][y] not in wall and (x-1,y) not in visited):
            queue.append((x-1,y))

        if (maze[x+1][y] not in wall and (x+1,y) not in visited):
            queue.append((x+1,y))
        d += 1

