kol = 1000
co = 0
for A in range(1, kol+1):
    k = 0
    for x in range(1, kol+1):
        if (A % 9 == 0) and ((280 % x == 0) <= ((A % x != 0) <= (730 % x != 0))):
            k += 1
    if k == kol:
        co += 1
print(co)