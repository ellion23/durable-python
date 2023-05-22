def check(s):
    global a, b, c, d
    if s == 'a':
        a = True
    elif s == 'b':
        b = True
    elif s == 'c':
        c = True
    elif s == 'd':
        d = True


n = int(input())
s = input()
vars = []
if 'a' not in s or 'b' not in s or 'c' not in s or 'd' not in s:
    print(-1)
    exit(0)
else:
    for k in range(n):
        a, b, c, d = [False for i in range(4)]
        temp = s[k]
        check(s[k])
        for i in range(k+1, n):
            temp += s[i]
            check(s[i])
            if all([a, b, c, d]):
                temp = temp[::-1]
                symbols = ['a', 'b', 'c', 'd']
                symbols.remove(temp[0])
                vars.append(max([temp.index(j) for j in symbols])+1)
                break
print(min(vars))
