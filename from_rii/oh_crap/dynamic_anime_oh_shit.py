f = open("kept_u_waiting_huh.txt", "r")
num = int(f.read())
meen = 1
laast = 0


def been(n, m, l):
    if n == m:
        if l == 1:
            return 1
        return 2
    if l == 1:
        return been(n, m + 1, 0)
    return been(n, m + 1, 0) + been(n, m + 1, 1)


print(been(num, meen, laast))
