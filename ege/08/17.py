numbers = [int(i) for i in open('17.txt').readlines()]
s = sum(numbers) / len(numbers)
count = 0
maxsum = 0
for i in range(len(numbers)-1):
    a = numbers[i]
    b = numbers[i + 1]
    if (min(a, b) < s) and ((a % 3 == 0 and a % 5 != 0 and a % 11 != 0 and a % 19 != 0) or (b % 3 == 0 and b % 5 != 0 and b % 11 != 0 and b % 19 != 0)):
        count += 1
        maxsum = max(maxsum, a + b)
print(count, maxsum)
