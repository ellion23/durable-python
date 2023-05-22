f = open('input1.txt', 'r')
w, h, n = map(int, f.readline().split())
l = 0
r = max(w, h) * n
lmin = 10 ** 9
m_opt = 0
m_prev = 0
while l != r:
    m = (l+r)//2
    n1 = m//w
    n2 = m//h
    if n1*n2 < n:
        l = m
    elif n1*n2 > n:
        if n1*n2<lmin:
            lmin = n1*n2
            m_opt = m
        r = m
    else:
        break
    if m == m_prev:
        break
    m_prev = m
print('m: ', m)
print('m_opt: ', m_opt)