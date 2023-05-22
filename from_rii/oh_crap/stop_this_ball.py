n = 5
s = [0 for i in range(n)]

def rec(i):
    if s[i-1] != 0:
        return s[i]
    if i == 0:
        s[i] = 1
        return 1
    elif i == 1:
        s[i] = rec(i-1) + 1
    elif i == 2:
        s[i] = rec(i-1) + rec(i-2)
    else:
        s[i] = rec(i-1) + rec(i-2) + rec(i-3)


rec(5)