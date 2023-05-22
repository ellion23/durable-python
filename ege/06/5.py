def f(n):
    digits = set([i for i in str(n)])
    k1 = str(min(digits.difference('0')))
    dig = digits.difference(k1)
    if len(digits) == 1:
        k2 = str(min(digits))
    else:
        k2 = str(min(dig))
    num1 = int(k1 + k2)

    digits = set([i for i in str(n)])
    k1 = str(max(digits.difference('0')))
    dig = digits.difference(k1)
    if len(digits) == 1:
        k2 = str(max(digits))
    else:
        k2 = str(max(dig))
    num2 = int(k1 + k2)
    return num2 - num1


count = 0
for i in range(300, 401):
    if abs(f(i)) == 20:
        count += 1
print(count)
