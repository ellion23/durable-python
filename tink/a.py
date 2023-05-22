data = [int(i) for i in input().split()]
if data == sorted(data) or data == sorted(data, reverse=True):
    print('YES')
else:
    print('NO')
