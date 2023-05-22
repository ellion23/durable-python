def F(n, m):
    if m == 0:
        d = 0
    else:
        d = n + F(n, m-1)
    return d


n, m = 0, 0
k = 0
for i in range(-150, 100000):
    n, m = i, i
    try:
        if F(n, m) == 30:
            k += 1
    except RecursionError:
        pass

print(k)



# # 82
# def f(n):
# 	if n <= 5: return n
# 	if n > 5 and n % 4 == 0:
# 		return n + f(n//2-1)
# 	if n > 5 and n % 4 != 0:
# 		return n + f(n+2)
#
#
# n  = 1
# while n < 100:
#     try:
#         print('n: {}, f(n): {}'.format(n, f(n))
#     except RecursionError:
#         pass
