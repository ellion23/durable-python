sumbadi = []
try:
    temp = sumbadi[0]
    sumbadi.pop(0)
except IndexError:
    print('Hey, bro, так не троллят.')

print(temp)