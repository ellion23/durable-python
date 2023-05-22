for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not x and z) or (not x and not y and not z)) == 1:
                print(x, y, z)
