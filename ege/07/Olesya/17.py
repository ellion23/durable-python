with open('/home/ellion/PycharmProjects/pythonProject/ege/07/17.txt') as f:
    n = [int(x) for x in f.readlines()]
count = 0
maxsum = -200000000
sred = sum(n)/len(n)
for i in range(1, len(n) - 1):
    a = n[i - 1]
    b = n[i]
    c = n[i + 1]
    if ((a or b or c) < sred) and (((a and b) % 7 == 0) or ((a and c) % 7 == 0) or ((b and c) % 7 == 0)):
        count += 1
        maxsum = max(maxsum, a + b + c)
print(count, maxsum)