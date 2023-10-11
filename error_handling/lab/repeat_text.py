entry = input()

try:
    repeat_time = int(input())
    print(entry * repeat_time)
except:
    print("Variable times must be an integer")
