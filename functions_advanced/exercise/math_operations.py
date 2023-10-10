from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)

    while numbers:
        num = numbers.popleft()
        kwargs['a'] += num

        if not numbers:
            break

        num = numbers.popleft()
        kwargs['s'] -= num

        if not numbers:
            break

        num = numbers.popleft()
        if num != 0:
            kwargs['d'] /= num

        if not numbers:
            break

        num = numbers.popleft()
        kwargs['m'] *= num

    result = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(result)
