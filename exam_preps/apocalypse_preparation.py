from collections import deque

healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

textiles = deque(int(x) for x in input().split(' '))
meds = [int(y) for y in input().split(' ')]

while textiles and meds:
    textile = textiles.popleft()
    med = meds.pop()
    sum_ = textile + med
    if sum_ == 30:
        healing_items["Patch"] += 1
    elif sum_ == 40:
        healing_items["Bandage"] += 1
    elif sum_ >= 100:
        healing_items["MedKit"] += 1

        if sum_ > 100:
            sum_ -= 100
            last_med = meds.pop()
            meds.append(last_med + sum_)
    else:
        meds.append(med + 10)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
elif not meds:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

result = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

for item, val in result:
    if val > 0:
        print(f"{item} - {val}")

if meds:
    meds = (str(i) for i in meds[::-1])
    print(f"Medicaments left:", ', '.join(meds))
if textiles:
    textiles = (str(i) for i in textiles)
    print(f"Textiles left:", ', '.join(textiles))