entry = [float(e) for e in input().split()]

result = {}

for num in entry:
    if num not in result:
        result[num] = 0
    result[num] = entry.count(num)

for num, count in result.items():
    print(f"{num} - {count} times")