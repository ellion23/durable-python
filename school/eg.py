# def f(x):
#     sx = str(x)
#     s12 = int(sx[0]) + int(sx[1])
#     s23 = int(sx[1]) + int(sx[2])
#     s34 = int(sx[2]) + int(sx[-1])
#     l = []
#     l.append(s12)
#     l.append(s23)
#     l.append(s34)
#     l.remove(min(l))
#     l.sort()
#     x = str()
#     for i in l:
#         x += str(i)
#     x = int(x)
#     return x
# z, x = 0, 1000
# while z != 1418:
#     x += 1
#     z = f(x)
# print(x)
# print(z)
# print(f(1599))
#
# # L = 0
# # x = -1
# # M = 0
# # while L != 3 and M != 28:
# #     x += 1
# #     while x > 0:
# #
# #         L = L + 1
# #
# #         if M < x:
# #
# #             M = M + (x % 10) * 2
# #
# #         x = x // 10
# #
# # print(L)
# #
# # print(M)




def F(n):

    if n > 2:

        return F(n-1)+ G(n-2)

    else: return 1

def G(n):

    if n > 2:

        return G(n-1) + F(n-2)

    else: return 1
print(F(8))