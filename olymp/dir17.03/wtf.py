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


s = 'abcabcd'
p = prefix(s)
print(*p)
