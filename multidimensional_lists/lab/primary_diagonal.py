n = int(input())

matrix = []
diagonal_sum = 0
for _ in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for row_index in range(n):
    diagonal_sum += matrix[row_index][row_index]

print(diagonal_sum)
