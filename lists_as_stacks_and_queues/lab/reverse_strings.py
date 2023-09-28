from collections import deque

entry = input()
stack = deque()

for ch in entry:
    stack.appendleft(ch)

print(''.join(stack))