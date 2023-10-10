def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == "even":
            kwargs[k] = [x for x in v if x % 2 == 0]
        else:
            kwargs[k] = [x for x in v if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda k: k[0]))



print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))
