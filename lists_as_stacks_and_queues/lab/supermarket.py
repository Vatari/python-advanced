from collections import deque

entry = input()
people = deque()

while entry != "End":
    if entry == "Paid":
        while people:
            print(people.popleft())
    else:
        people.append(entry)
    entry = input()

print(f"{len(people)} people remaining.")
