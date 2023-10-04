rows = int(input())

matrix = []

for row in range(rows):
    elements = list(input())
    matrix.append(elements)

searched_element = input()

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element == searched_element:
            print((row_index, col_index))
            exit()

print(f"{searched_element} does not occur in the matrix")