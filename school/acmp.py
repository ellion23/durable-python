# 529
# from math import hypot
# x, y, z, w = map(int, input().split())
# print(hypot((z - x), (w - y)))
# l, w, h = map(int, input().split())
# print(round((w*h + l*h)*2 / 16))
# чёт/нечет
# x = int(input())
# if x%2==0:
#     print('чёт')
# else:
#     print('неч')


# x, y, z = map(int, input().split())
# if (94 < x < 727) and (94 < y < 727) and (94 < z < 727):
#   print(max(x, y, z))
# else:
#   print('Error')

# a = int(input())
# a = list(str(131072 / a))
# if a[-1] == '0':
#     print('YES')
# else:
#     print('NO')



# a = int(input())
# l2 = list()
# l = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192']
# for i in list(l):
#     if a == int(i):
#         print('YES')
#     l2.append(a == int(i))
# if l2 == [False, False, False, False, False, False, False, False, False, False, False, False, False, False]:
#     print('NO')



w, h, r = map(int, input().split())
if (r <= w) and (r <= h):
    print('YES')
else:
    print('NO')