from collections import deque

armor_queue = deque([int(x) for x in input().split(',')])
attacks = [int(x) for x in input().split(',')]

killed_monsters = 0
while armor_queue and attacks:
    curr_armor = armor_queue.popleft()
    curr_attack = attacks.pop()
    if curr_attack >= curr_armor:
        killed_monsters += 1
        curr_attack -= curr_armor
        if attacks:
            attacks[-1] += curr_attack
        elif not attacks and curr_attack > 0:
            attacks.append(curr_attack)
    else:
        curr_armor -= curr_attack
        armor_queue.append(curr_armor)

if not armor_queue:
    print("All monsters have been killed!")
if not attacks:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")

