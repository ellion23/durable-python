for x in range(1, 10000):
    xst = x
    K = 0
    R = 9
    y = x % 10
    while x > 0:
        K = K + 1
        if R > (x % 10):
            R = x % 10
        x = x // 10
    R = y - R
    if K == 4 and R == 3:
        print(xst)