
numbers = [int(x) for x in open('in.txt').readlines()]
d = 160
count = 0
maxsum = 0
len_numbers = 4000
for i in range(len_numbers - 1):
    for j in range(i+1, len_numbers):
        if ((numbers[i] % d) != (numbers[j] % d)) and ((numbers[i] % 7 == 0) or (numbers[j] % 7 ==0)):
            count += 1
            maxsum = max(maxsum, numbers[i] + numbers[j])

print(count, maxsum)
