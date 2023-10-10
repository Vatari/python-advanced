def kwargs_length(**kwargs):
    return len(kwargs)


dict_ = {"name": "Peter", "age": 25}
print(kwargs_length(**dict_))
