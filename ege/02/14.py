def sys_num(n, k):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


n = 123
for i in range(2, 11):
    print(sys_num(n, i), i)