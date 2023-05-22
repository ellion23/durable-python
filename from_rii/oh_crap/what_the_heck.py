from collections import deque
q = deque()
f = open('kept_u_waiting_huh.txt', 'r')
n = int(f.readline())
a_min = 9999
k = 6
s_min = a_min ** 2
for si in f.readlines():
    a_i = int(si.rstrip())
    # print(a_i)
    q.append(a_i)
    if len(q) > k:
        a = q.popleft()
        if a % 2 == 1 and a < a_min:
            a_min = a

    if a_i % 2 == 1:
        s_min = min(s_min, a_i * a_min)

print(s_min)
