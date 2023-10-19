def make_a_move(row_, col_, matrix):
    hazelnuts_found = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        hazelnuts_found += 1
    matrix[row_][col_] = '*'
    return hazelnuts_found, matrix


rows = int(input())
directions = input().split(", ")
field = []
collected_hazelnuts = 0
is_trapped = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for direction in directions:
    if direction == 'left':
        squirrel_position[1] -= 1
    elif direction == 'right':
        squirrel_position[1] += 1
    elif direction == 'down':
        squirrel_position[0] += 1
    elif direction == 'up':
        squirrel_position[0] -= 1
    result = make_a_move(squirrel_position[0], squirrel_position[1], field)
    if not result:
        is_trapped = True
        break
    hazelnuts, field = result[0], result[1]
    collected_hazelnuts += hazelnuts
    if collected_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not is_trapped and collected_hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")