def func(n):
    bi = bin(n-1)[2:]
    bi = '0' * (8 - len(bi)) + bi
    bi = bi.replace('1', '2')
    bi = bi.replace('0', '1')
    bi = bi.replace('2', '0')
    return int(bi, 2)


x = 1
while func(x) != 143:
    x += 1
print(x, func(x))
