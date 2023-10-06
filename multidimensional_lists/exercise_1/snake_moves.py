from collections import deque

row, col = [int(x) for x in input().split()]
entry = deque(input())

matrix = []

for r in range(row):
    matrix.append([''] * col)
    for c in range(col):
        if r % 2 == 0:
            matrix[r][c] = entry[0]
        else:
            matrix[r][-1 - c] = entry[0]
        entry.rotate(-1)

[print(*row, sep='') for row in matrix]