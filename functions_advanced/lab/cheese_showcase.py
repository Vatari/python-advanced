def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda k: (-len(k[1]), k[0]))
    result = ''

    for name, qty in sorted_cheese:
        result += f"{name}\n"
        sorted_items = sorted(qty, reverse=True)
        result += "\n".join([str(el) for el in sorted_items])
        result += "\n"
    return  result


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125]))
