def binary_search1(lst: list, n1: int, m1: int, ):
    l = 0
    r = max_t
    found_delay = 0
    while True:
        m1 = (l+r)//2
        total_count = 0
        current_time = m1
        for j in range(n1):
            count = binary_search2(lst[j], current_time)
            current_time += lst[j][0]
            total_count += count
        if total_count >= capacity:
            r = m1
        else:
            l = m1
        if total_count == capacity:
            found_delay = m1
        else:
            if total_count<capacity and m1 == found_delay-1:
                break
    return found_delay


def binary_search2(lst: list, time: int) -> int:
    max_people = 0
    l = 2
    r = lst[1]+1
    while l != r:
        m = (l+r)//2
        if lst[m] <= time and lst[m+1] > time:
            max_people = m-1
            break
        elif lst[m+1] <= time and m+1 == lst[1]+1:
            max_people = m
            break
        if lst[m] < time:
            l=m
        else:
            r = m
    return max_people
if __name__ == '__main__':
    f = open('bez_raznitsy_kak.txt', 'r')
    n, m = map(int, f.readline().split())

    st = [[] for i1 in range(n)]
    maxt = 0
    for i in range(n):
        st[i] = list(map(int, f.readline().split()))
        if max(st[i][2:]) > maxt:
            maxt = max(st[i][2:])

    t = binary_search1()