# n = int(input())
n = 3000
matrix = [[0 for i in range(n)] for j in range(n)]
right, left, down, up = 0, 1, 2, 3


direction = right
a, b = 0, 0
for i in range(1, n**2+1):
    matrix[a][b] = i
    if direction == right:
        if b == n-1 or matrix[a][b+1] != 0:
            direction = down
            a += 1
        else:
            b += 1
    elif direction == down:
        if a == n-1 or matrix[a+1][b] != 0:
            direction = left
            b -= 1
        else:
            a += 1
    elif direction == left:
        if b == n-1 or matrix[a][b-1] != 0:
            direction = up
            a -= 1
        else:
            b -= 1
    elif direction == up:
        if a == n-1 or matrix[a-1][b] != 0:
            direction = right
            b += 1
        else:
            a -= 1

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()
