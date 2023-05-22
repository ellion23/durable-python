for n in range(1000, 2000):
  x = n
  a = -1
  while n > 9 and a != n % 10:
    a = n % 10
    n //= 10
  if n % 10 == 4:
    print(x)