def sys_num(n, k: int = 4):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


n = 3 * 16**8 - 4**5 + 3
print(sys_num(n).count('3'))