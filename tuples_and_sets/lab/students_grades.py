n = int(input())

students = {}

for _ in range(n):
    student, grade = input().split()
    if student not in students:
        students[student] = []

    students[student].append(float(grade))

for student, grade in students.items():
    avg = sum(grade) / len(grade)
    print(f"{student} -> {' '.join([str(f'{g:.2f}') for g in grade])} "f"(avg: {avg:.2f})")
