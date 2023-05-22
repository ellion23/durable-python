def sys_num(n, k=7):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s


def check_pairs(n1, n2):
    global maximum, k
    bin_sum = sys_num(n1 + n2)
    check_sum = bin_sum == bin_sum[::-1]
    if check_sum:
        k += 1
        if maximum < n1 + n2:
            maximum = n1 + n2


numbers = []
f = open('17.txt', 'r')
for g in range(1000):
    numbers.append(int(f.readline()))
maximum, k = 1, 0
for i in range(999):
    check_pairs(numbers[i], numbers[i + 1])
print(k, sys_num(maximum))
