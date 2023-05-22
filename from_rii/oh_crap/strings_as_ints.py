# -*- coding: utf-8 -*-
def hash(s: str, p: int) -> int:
    f = 0
    pow_i = 1
    for i in range(len(s)):
        f += (ord(s[i])-ord('a'))*pow_i
        pow_i *= p
    return f


f = open('hashhhing.txt', encoding='utf8')
txt = list(map(str, f.read().split()))
nmbrs = list()
unic = list()

for i in range(len(txt)):
    txt_now = hash(txt[i].lower(), 31)
    if txt_now not in nmbrs:
        nmbrs.append(txt_now)
        unic.append(txt[i])

for i in range(len(nmbrs)):
    print('{}: {}'.format(nmbrs[i], unic[i]))
print(len(txt), len(nmbrs))