entry = input().split("|")

matrix = []

for i in range(len(entry) - 1, -1, -1):
    row = [int(x) for x in entry[i].split()]
    if row:
        matrix.append(row)


[print(*row, sep=" ", end=" ") for row in matrix]
