numbers = [int(i.strip()) for i in open('17.txt').readlines() if i != '\n']
sarph = sum(numbers) / 2000
count, minsum = 0, 100000
for i in range(1999):
    n1, n2 = numbers[i], numbers[i+1]
    if (n1 < sarph or n2 < sarph) and ('7' in str(n1) or '7' in str(n2)):
        count += 1
        if minsum > n1 + n2:
            minsum = n1 + n2
print(count, minsum)
