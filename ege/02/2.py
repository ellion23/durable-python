for a in range(2):
    for c in range(2):
        for b in range(2):
            if (a or not c) or (b or c):
                print(a, b, c)