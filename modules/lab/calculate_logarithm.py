from math import log

num = int(input())
entry = input()

result = log(num) if entry == 'natural' else log(num, int(entry))
print(result)