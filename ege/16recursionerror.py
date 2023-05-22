def f(n):
    if n <= 5:
        return n
    elif n > 5 and n % 3 == 0:
        return n + f(n / 3 + 2)
    else:
        return n + f(n + 3)


for i in range(1001):
    try:
        if f(i) > 1000:
            print(f(i), i)
    except:
        pass


fuckin_list = [0, 0, 1, 3, 2, 4, 0, 1, 0, 134, 23]
for g in fuckin_list:
    try:
        print(17 / g)
    except:
        pass
