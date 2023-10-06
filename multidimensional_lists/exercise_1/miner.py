def is_valid(r, c, matrix_size):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


n = int(input())
commands = input().split()

matrix = []
current_row = 0
current_col = 0
coal = 0
is_game_over = False

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 's':
            current_row, current_col = row, col  # miner position
        elif matrix[row][col] == 'c':  # coal position
            coal += 1

for command in commands:
    if command == 'up':
        if is_valid(current_row - 1, current_col, n):
            current_row -= 1
    elif command == 'down':
        if is_valid(current_row + 1, current_col, n):
            current_row += 1
    elif command == 'left':
        if is_valid(current_row, current_col - 1, n):
            current_col -= 1
    elif command == 'right':
        if is_valid(current_row, current_col + 1, n):
            current_col += 1

    if matrix[current_row][current_col] == 'e':
        print(f"Game over! ({current_row}, {current_col})")
        is_game_over = True
        break
    if matrix[current_row][current_col] == 'c':
        coal -= 1
        matrix[current_row][current_col] = '*'
        if coal == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            is_game_over = True
            break

if not is_game_over:
    print(f"{coal} pieces of coal left. ({current_row}, {current_col})")