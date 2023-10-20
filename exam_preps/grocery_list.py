def shop_from_grocery_list(budget_, grocery_lst, *prices):
    bought_products = []
    for prod, price in prices:
        if prod in grocery_lst:
            if budget_ >= price:
                if prod not in bought_products:
                    budget_ -= price
                    bought_products.append(prod)
                    grocery_lst.remove(prod)

    if len(grocery_lst) > 0:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_lst)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget_:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
