for s in range(1, 10000):
  start = s
  n = 10
  while s > n + 20:
    s = s - 6
    n = n + 11
  if n >= 450:
    print(start, n)
    exit(0)