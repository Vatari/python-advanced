n = int(input())

uniques = set()

for _ in range(n):
    name = input()
    uniques.add(name)

print(*uniques, sep='\n')