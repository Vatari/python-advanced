def grocery_store(**kwargs):
    receipt = dict(sorted(kwargs.items(), key=lambda k: (-k[1], -len(k[0]), k[0])))
    result = []
    for prod, qty in receipt.items():
        result.append(f"{prod}: {qty}")
    return "\n".join(result)


print(grocery_store(bread=5, pasta=12, eggs=12))
