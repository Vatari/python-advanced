from functools import reduce


def operate(operator, *args):
    return reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)  # EVAL SOLUTION

    # def add():
    #     return reduce(lambda a, b: a + b, args)

    # def subtract():
    #     return reduce(lambda a, b: a - b, args)
    #
    # def multiply():
    #     return reduce(lambda a, b: a * b, args)
    #
    # def divide():
    #     return reduce(lambda a, b: a / b, args)
    #
    # if operator == "+":
    #     return add()
    # elif operator == "-":
    #     return subtract()
    # elif operator == "*":
    #     return multiply()
    # elif operator == "/":
    #     return divide()

#MAPPER SOLUTION
# mapper = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }

#print(mapper[operator][collection])


print(operate("-", 3, 4, 5))
