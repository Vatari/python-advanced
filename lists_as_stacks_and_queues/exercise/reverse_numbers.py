from collections import deque

entry = deque((input().split()))

for i in range(len(entry)):
    print(entry.pop(), end=' ')
