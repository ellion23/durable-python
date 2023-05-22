f = open('kept_u_waiting_huh.txt')
n, w = map(int, f.readline().split())
p = []
e = []


def first(p, n, w, f, e):
    for i in range(n):
        p.append(list(map(int, f.readline().split())))
    for i in range(n+1):
        e.append([0] * (w+1))

    for d in range(1, n+1):
        for s in range(w+1):
            e[d][s] = e[d-1][s]
            if s >= p[d-1][1] and e[d-1][s-p[d-1][1]] + p[d-1][0] > e[d-1][s]:
                e[d][s] = e[d-1][s-p[d-1][1]] + p[d-1][0]
    return e[d][s]


def second(p, n, w, f, e):
    for i in range(n):
        p.append(list(map(int, f.readline().split())))
    e = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(1, n):
        for c in range(w+1):
            e[i][c] = e[i-1][c]
            if p[i][1] <= c:
                e[i][c] = max(e[i][c], e[i][c-p[i][1]]+p[i][0])
    return e[i][c]



print(second(p, n, w, f, e))
