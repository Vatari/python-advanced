n = int(input())

cars = set()

for _ in range(n):
    command, car_plate = input().split(', ')
    if command == "IN":
        cars.add((car_plate))
    elif command == "OUT":
        cars.remove(car_plate)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")
