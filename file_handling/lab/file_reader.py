import os

WORK_DIR = os.path.abspath(__file__)
file_path = os.path.join(WORK_DIR, "numbers.txt")

if not os.path.isfile("numbers.txt"):
    with open("numbers.txt", 'w') as f:
        for i in range(1, 6):
            f.writelines(f"{i}\n")

with open("numbers.txt", 'r') as f:
    for num in f:
        print(num, end='')