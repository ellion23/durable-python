for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not ((x <= y) <= w) and z) == 1:
                    print(f'x: {x}, y: {y}, z: {z}, w: {w}')