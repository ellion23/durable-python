for s in range(1, 10000):
    n = 1
    while s < 28:
      s = s + 5
      n = n * 3
    if n == 81:
        print(s, n)