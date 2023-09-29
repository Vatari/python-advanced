from collections import deque

entry = deque(input())
opening = '([{'
closing = ')]}'
counter = 0

while entry and counter < len(entry) / 2:
    if entry[0] not in opening:
        break
    index = opening.index(entry[0])
    if entry[1] == closing[index]:
        entry.popleft()
        entry.popleft()
        entry.rotate(counter)
        counter = 0
    else:
        entry.rotate(-1)
        counter += 1

if entry:
    print("NO")
else:
    print("YES")
