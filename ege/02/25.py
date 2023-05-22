# [2358827; 2358891]
l = []
g = 1
for i in range(2358827, 2358892):
    for k in range(1, i // 2 + 1):
        if i % k == 0:
            g += 1
    if g == 2:
        print(i)
        g = 1
    else:
        g = 1