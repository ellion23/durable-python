def f(n):
    b = bin(n)[2:]
    if b.count('1') > b.count('0'):
        b += '0'
    else:
        b += '1'
    if len(b) % 2 == 0:
        b = b[:len(b)//2-1] + b[len(b)//2+1:]
    else:
        mid = len(b) // 2
        b = b[:mid-1] + b[mid+2:]
    return int(b, 2)


x = 195
# while True:
#     if f(x) == 55:
#         break
#     x += 1
print(x, f(x))
