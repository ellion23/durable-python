from collections import deque

f = open('ex3.txt')
r = f.readline()
l = deque(r)
print(l)

