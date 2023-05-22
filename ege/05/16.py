def f(n):
    if n < 2:
        return n
    elif n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    elif n >= 2 and n % 2 == 1:
        return f(3*n + 1) + 1


k, l = 0, []
for i in range(1, 101):
    if f(i) > 100:
        l.append(i)
        k += 1
print(l, k)
