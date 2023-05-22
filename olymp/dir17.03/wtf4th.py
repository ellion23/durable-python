def prefix(s) -> int:
    n = len(s)
    p = [0 for i in range(n)]
    p[0] = 0
    for i in range(1, n):
        j = p[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


s = 'abababababababababababababababab'
p = prefix(s)
print(*p)
n = len(s)
print(s[0:n-p[n-1]])
print(n-p[n-1])
# for i in range(1, n+1):
#     t = s[:i]
#     p = prefix(t+'#'+s)
#     print(*p)