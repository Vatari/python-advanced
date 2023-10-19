def accommodate_new_pets(capacity: int, max_weight: float, *pets):
    pets_accommodated = {}
    result = []

    for pet_type, pet_weight in pets:
        if capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in pets_accommodated:
            pets_accommodated[pet_type] = 0
        pets_accommodated[pet_type] += 1
        capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(pets_accommodated.items())]
    return '\n'.join(result)