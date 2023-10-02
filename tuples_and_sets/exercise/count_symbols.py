entry = input()

occurences = {}

for s in entry:
    if s not in occurences:
        occurences[s] = 0
    occurences[s] = entry.count(s)

sorted_keys = list(occurences)
sorted_keys.sort()
result = {i: occurences[i] for i in sorted_keys}
for occ, count in result.items():
    print(f"{occ}: {count} time/s")