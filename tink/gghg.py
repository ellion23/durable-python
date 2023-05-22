def a():
    global l
    s = 0
    for i in l:
        s += i[0]
    return s


n, s = map(int, input().split())
l = []
for i in range(n):
    l.append([i for i in map(int, input().split())])
i = n // 2
l.sort()
while a() < s:
    if l[i][0] < l[i][1] and i < n-1:
        l[i][0] += 1
        i += 1
    elif i < n-1:
        i += 1
    elif i == n-1:
        l.sort()
        i = n // 2 - 1
    else:
        break

l.sort()
print(l[n//2][0])
