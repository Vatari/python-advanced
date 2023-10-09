from collections import deque


def fill_the_box(*args):
    height, length, width = args[:3]
    box_size = height * length * width
    rest = list(args[3:])
    temp = []

    for num in range(0, len(rest)):
        current = rest[0]
        temp.append(rest.pop(0))

        if current == "Finish":
            break
        box_size -= current
        if box_size < current:
            return f"No more free space! You have {sum([x for x in rest if x != 'Finish']) - box_size} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
