def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]

    result = sorted(persons.items(), key=lambda k: k[0])
    final = []
    for name, age in result:
        final.append(f"{name} is {age} years old.")
    return "\n".join(final)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Ivan", "Stoyan", I=20, S=29))
