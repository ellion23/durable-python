f = open('kept_u_waiting_huh.txt', 'r')
l = int(f.readline())
c = list(map(int, f.read().split()))
n = 0
for i in range(l):
    n += c[i]
print('{}:{:02d}'.format(n//60, n%60))