s = 2022 * '1'
while 5*'1' in s or '555' in s:
    if 5 * '1' in s:
        s = s.replace(5*'1', '555', 1)
    else:
        s = s.replace('555', '5')

print(s)
