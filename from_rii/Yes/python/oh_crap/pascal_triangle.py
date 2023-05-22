f = open('kept_u_waiting_huh.txt', 'r')
n = int(f.readline())
triangle = list()
def line_now(n):
    line = list()
    for i in range(n):
        if i == n-1 or i == 0:
            line.append(1)
        else:
            current_line = line_now(n-1)
            line.append(current_line[i-1]+current_line[i])
    return line

for i in range(n):
    triangle.append(line_now(i))
triangle.pop(0)
print(*triangle, end=' ')