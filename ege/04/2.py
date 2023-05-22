for a in range(2):
    for b in range(2):
        for c in range(2):
            if (not (not a or b) or (not a and c)) == 1:
                print(a, b, c)
