board_size = int(input())

matrix = []
knights = []

for row in range(board_size):
    matrix.append([x for x in input()])
    for col in range(board_size):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1),
]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        current_hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                if matrix[new_row][new_col] == "K":
                    current_hits += 1
        if current_hits > max_hits:
            max_hits = current_hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
