rows, cols = [int(x) for x in input().split(', ')]

matrix = []
sum_columns = 0

for row in range(rows):
    elements = [int(el) for el in input().split()]

    matrix.append(elements)


def sum_cols(matrix, i):
    return sum([row[i] for row in matrix])


for i in range(cols):
    print(sum_cols(matrix, i))
