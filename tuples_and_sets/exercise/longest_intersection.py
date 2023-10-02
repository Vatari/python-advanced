n = int(input())

longest = set()

for _ in range(n):
    range1, range2 = input().split('-')
    first_start, first_end = [int(x) for x in range1.split(',')]
    second_start, second_end = [int(y) for y in range2.split(',')]

    set1 = set(range(first_start, first_end + 1))
    set2 = set(range(second_start, second_end + 1))
    intersection = set1 & set2

    if len(intersection) > len(longest):
        longest = intersection

print(f"Longest intersection is {list(longest)} with length {len(longest)}")