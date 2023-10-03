from collections import deque

colors = deque(input().split())

main_colors = ['red', 'blue', 'yellow']
additional_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['blue', 'yellow'], }

final_colors = []

while colors:
    str1 = colors.popleft()
    str2 = colors.pop() if colors else '' # ternary operator
    if str1 + str2 in main_colors or str1 + str2 in additional_colors:
        final_colors.append(str1 + str2)
    elif str2 + str1 in main_colors or str2 + str1 in additional_colors:
        final_colors.append(str2 + str1)
    else:
        if len(str1) > 1:
            colors.insert(len(colors) // 2, str1[:-1])
        if len(str2) > 1:
            colors.insert(len(colors) // 2, str2[:-1])

for c in final_colors:
    if c in additional_colors:
        for color in additional_colors[c]:
            if color not in final_colors:
                final_colors.remove(c)
                break

print(final_colors)