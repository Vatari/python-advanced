from collections import deque

boxes = deque([int(b) for b in input().split()])
rack_capacity = int(input())
racks = 1
current_rack_capacity = rack_capacity

while boxes:
    current_cloth = boxes[-1]
    if current_cloth <= rack_capacity:
        rack_capacity -= current_cloth
        boxes.pop()
    else:
        racks += 1
        rack_capacity = current_rack_capacity
print(racks)
