def sys_num(n, k: int = 9):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


n = 81**5 + 3**30 - 27
print(sys_num(n).count('8'))
