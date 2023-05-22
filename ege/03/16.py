def F(n):
  global count
  count += 1
  if n > 0:
    G(n - 1)

def G(n):
  global count
  count += 1
  if n > 1:
    F(n - 2)


count = 0
F(13)
print(count)

