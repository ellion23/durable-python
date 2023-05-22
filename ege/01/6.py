def func(s):
  while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('2222', '333', 1)
    s = s.replace('33', '1', 1)
  return s


ss = 99*'1'
l = []
for i in range(30):
  l.append([func(ss + '1'*i), len(ss + '1'*i)])

for k in l:
  if k[0].count('1') == 0:
    print(k)