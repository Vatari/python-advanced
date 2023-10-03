set1 = set(int(x) for x in input().split())
set2 = set(int(y) for y in input().split())

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + ' ' + line[1]
    nums = [int(n) for n in line[2:]]

    if command == "Add First":
        set1.update(nums)
    elif command == "Add Second":
        set2.update(nums)
    elif command == "Remove First":
        set1.difference_update(nums)
    elif command == "Remove Second":
        set2.difference_update(nums)
    elif command == "Check Subset":
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')