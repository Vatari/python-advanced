#from functools import reduce

rows = int(input())

flatened_matrix = []

for i in range(rows):
    #element = [y for el in [input().split(', ')] for y in el]
    elements = [el for el in input().split(', ')]
    for j in elements:
        flatened_matrix.append(int(j))

print(flatened_matrix)


# a = list(map(lambda x: [int(y) for y in x], list(map(lambda x: x.split(', '), list(filter(lambda x: x != "", matrix.split("\n")))))))
# print(a)

# rows = int(input())
# matrix = [input().split("\n") for _ in range(rows)]
#
# a = list(map(lambda x: int(x), reduce(lambda a, b: a+b, [x[0].split(", ") for x in matrix])))
# print(a)