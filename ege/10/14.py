def sys_num(n, k: int = 5):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


mnum = 5**2022 - 2*5**1010 + 25**550 + 2500

print(sys_num(mnum).count('4'))
