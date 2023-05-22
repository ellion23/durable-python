f = open('inpoot.txt', 'r')
n = int(f.readline())
cost = [0] + list(map(int, f.readline().split()))
s = [0 for i in range(n+1)]

s[1] = cost[1]

for i in range(2, len(cost)):
    s[i] = min(s[i-1], s[i-2]) + cost[i]

print(*s)