while True:
    edges_raw = list(map(int, input().split()))
    edges = sorted(edges_raw, reverse=True)
    if edges[0] == edges[1] == edges[2] == 0:
        break
    if edges[0] ** 2 == edges[1] ** 2 + edges[2] ** 2:
        print('right')
    else:
        print('wrong')