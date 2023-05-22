k = int(input())
n = int(input())
if n == 0:
    print(0)
elif n < k:
    a1 = abs(n - k)
    print(min(a1, n))
elif n == k:
    print(0)
else:
    a1 = abs(n - (n//k * k) - k)
    a2 = abs(n - (n//k * k))
    print(min(a1, a2))