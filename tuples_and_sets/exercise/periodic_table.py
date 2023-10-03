n = int(input())

uniques = set()

for _ in range(n):
    items = input().split()
    for item in items:
        uniques.add(item)

print(*uniques, sep='\n')