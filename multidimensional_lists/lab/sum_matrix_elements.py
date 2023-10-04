rows, cols = [int(y) for y in input().split(', ')]

matrix = []
total_sum = 0

for _ in range(rows):

    elements = [int(x) for x in input().split(', ')]
    total_sum += sum(elements)
    matrix.append(elements)

print(total_sum)
print(matrix)