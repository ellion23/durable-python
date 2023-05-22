import math
nums = [int(i) for i in open('ege/10/17var1.txt')]
count = 0
sqrs = []
maxsum = 0
i = 1
while True:
    if i**2 > 10000:
        break
    sqrs.append(i**2)
    i += 1

for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    if a in sqrs or b in sqrs:
        maxsum = max(maxsum, a + b)
        count += 1

print(count, maxsum)
