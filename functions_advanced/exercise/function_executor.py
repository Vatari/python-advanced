def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")
    return "\n".join(result)


def sum_numbers(n1, n2):
    return n1 + n2


def multiply_numbers(n1, n2):
    return n1 * n2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
