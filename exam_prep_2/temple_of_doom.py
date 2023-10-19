from collections import deque

tools = deque([int(t) for t in input().split()])
substances = [int(s) for s in input().split()]
challenges = [int(c) for c in input().split()]

while challenges and substances:
    curr_tool = tools.popleft()
    curr_substance = substances[-1]
    curr_product = curr_tool * curr_substance
    if curr_product in challenges:
        challenges.remove(curr_product)
        substances.pop()
        continue
    curr_tool += 1
    tools.append(curr_tool)
    substances[-1] -= 1
    if substances[-1] == 0:
        substances.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(t) for t in tools])}")
if substances:
    print(f"Substances: {', '.join([str(s) for s in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")