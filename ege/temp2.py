nums = [i for i in range(10000, 100000)]

def f(word):
    ws = [i for i in word]
    if ws == sorted(ws):
        return True
    else:
        return False


count = 0
for g in nums:
    if f(hex(g)[2:]) is True:
        count += 1

print(count)
