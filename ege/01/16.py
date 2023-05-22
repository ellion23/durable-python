def f(n):
    if n <= 3: return n
    elif  n > 3 and n % 2 == 0:
        return 2*n + f(n-1)
    elif n > 3 and n % 2 != 0:
        return n*n + f(n-2)


k = 0
for n in range(1, 101):
    if f(n) % 3 == 0:
        k += 1

print(k)