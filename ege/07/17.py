# 17
numbers = [int(i) for i in open('/home/ellion/PycharmProjects/pythonProject/ege/07/17.txt').readlines()]
s = sum(numbers) / len(numbers)
count, maxsum = 0, 0
for i in range(len(numbers)-2):
    a = numbers[i]
    b = numbers[i+1]
    c = numbers[i+2]
    isdel = [a % 7 == 0, b % 7 == 0, c % 7 == 0]
    if (min(a, b, c) < s) and isdel.count(True) >= 2:
        count += 1
        maxsum = max(maxsum, a + b + c)
print(count, maxsum)
