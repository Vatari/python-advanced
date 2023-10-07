matrix_size = int(input())

matrix = []
alice = []

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
tea = 0

while tea < 10:
    command = input()
    move = possible_moves[command]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or row >= matrix_size or col < 0 or col >= matrix_size:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in "*.":
        tea += int(matrix[row][col])
    matrix[row][col] = "*"
    alice = [row, col]

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row, sep=" ") for row in matrix]
