s = '3' * 147
while '5555' in s or '3333' in s:
    if '5555' in s:
        s = s.replace('5555', '3', 1)
    else:
        s = s.replace('3333', '5')
print(s)