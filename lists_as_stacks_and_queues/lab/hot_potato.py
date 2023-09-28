from collections import deque

entry = deque(input().split())
rotations = int(input()) - 1

for i in range(len(entry)):
    while len(entry) > 1:
        entry.rotate(-rotations)
        print(f"Removed {entry.popleft()}")

print(f"Last is {''.join(entry)}")
