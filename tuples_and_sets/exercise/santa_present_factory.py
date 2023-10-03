from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(y) for y in input().split())

points = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
presents_ready = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents_ready:
            presents_ready[new_present] = 0
        presents_ready[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()

if ('Doll' in presents_ready and 'Wooden train' in presents_ready) or ('Teddy bear' in presents_ready and 'Bicycle' in presents_ready):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f" Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy, count in sorted(presents_ready.items()):
    if count > 0:
        print(f"{toy}: {count}")