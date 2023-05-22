def sys_num(n, k):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


num = 9**8 + 3**24 - 18
print(sys_num(num, 3).count('2'))

