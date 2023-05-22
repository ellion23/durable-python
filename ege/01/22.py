k = 0
for x in range(1, 1000):
    a = 0
    b = 1
    while x > 0:
      a = a + 1
      b = b * (x % 10)
      x = x // 10
    if a == 2 and b == 12:
        k += 1
print(k)