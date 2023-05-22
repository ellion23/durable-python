for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w and y) or ((not x or w) == (not y or z))) == 0:
                    print('x, y, z, w ', x, y, z, w)
