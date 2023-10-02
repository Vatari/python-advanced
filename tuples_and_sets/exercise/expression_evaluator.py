from collections import deque

entry = input().split()
numbers = deque()

for s in entry:
    if s not in '+-*/':
        numbers.append(int(s))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if s == "+":
                result = first_number + second_number
                numbers.appendleft(result)
            elif s == "-":
                result = first_number - second_number
                numbers.appendleft(result)
            elif s == "*":
                result = first_number * second_number
                numbers.appendleft(result)
            else:
                result = first_number // second_number
                numbers.appendleft(result)

           # result = str(first_number) + s + str(second_number)    # ----> EVAL SOLUTION
           # numbers.appendleft(eval(result))

print(numbers[0])