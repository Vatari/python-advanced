number_of_guests = int(input())

reservations = set()

for _ in range(number_of_guests):
    reservation = input()
    reservations.add(reservation)

command = input()
while command != "END":
    if command in reservations:
        reservations.remove(command)
    command = input()

print(len(reservations))
reservations = sorted(reservations)
print(*reservations, sep='\n')
