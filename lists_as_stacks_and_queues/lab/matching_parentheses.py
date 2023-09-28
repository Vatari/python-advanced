entry = input()
stack = []

for i in range(len(entry)):
    if entry[i] == "(":
        stack.append(i)
    elif entry[i] == ")":
        last_parentheses = stack.pop()
        print(entry[last_parentheses:i + 1])