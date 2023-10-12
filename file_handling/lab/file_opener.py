import os

WORK_DIR = os.path.abspath(__file__)
file_path = os.path.join(WORK_DIR, "text.txt")

if not os.path.isfile('text.txt'):
    with open("text.txt", 'w') as f:
        f.writelines("This is some random line \n")
        f.writelines("This is the second line \n")
        f.writelines("And this is the third one \n")

try:
    with open("text.txt", 'r'):
        print("File found")
except FileNotFoundError:
    print("File not found")

