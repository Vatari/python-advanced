from collections import deque

num = int(input())
stack = deque()
lst = []

for q in range(num):
    query = input().split()
    if query[0] == "1":
        number = query[1]
        stack.appendleft(int(number))
    elif query[0] == "2":
        if stack:
            stack.popleft()
    elif query[0] == "3":
        if stack:
            print(max(stack))
    elif query[0] == "4":
        if stack:
            print(min(stack))
    else:
        break

stack = [str(i) for i in stack]
print(", ".join(stack))

