symbols = ["-", ",", ".", "!", "?"]

with open('../line_numbers/text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for symbol in symbols:
                result = result.replace(symbol, '@')
            print(result)