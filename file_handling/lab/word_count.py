import os
import re

output = {}

if not os.path.isfile("words.txt"):
    with open("words.txt", 'w') as f:
        f.write("quick is fault")

if not os.path.isfile("input.txt"):
    with open("input.txt", 'w') as f:
        f.writelines("-I was quick to judge him, but it wasn't his fault.\n"
                     "-Is this some kind of joke?! Is it?\n"
                     "-Quick, hide here…It is safer.")

with open('words.txt', 'r') as f:
    searched_words = [word for word in f.read().split()]

with open('input.txt', 'r') as f:
    words = f.read().lower()

for word in searched_words:
    pattern = rf"\b{word}\b"
    result = re.findall(pattern, words)
    output[word] = len(result)

for w, c in output.items():
    with open('output.txt', 'a') as f:
        f.write(f"{w} - {c}\n")
