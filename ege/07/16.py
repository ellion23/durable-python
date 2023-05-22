def f(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    else:
        return f(n-1) + n


for i in range(10000):
    if f(i) == 19:
        print(i, f(i))
        break
x = 1
while f(x) != 19:
    x += 1
print(x, f(x))

