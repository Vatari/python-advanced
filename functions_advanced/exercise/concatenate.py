def concatenate(*args, **kwargs):
    result = ""
    for str_ in args:
        result += str_
    for k, v in kwargs.items():
        if k in result:
            result = result.replace(k, v)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
