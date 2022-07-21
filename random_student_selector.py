import random
from student_list import students


def choose_random_student(students_list):
    student = random.choice(students_list)
    return student


# Main
accept = "n"
while accept.lower() == 'n':
    navigator = choose_random_student(students)
    accept = input(f"The navigator chosen is : {navigator}. Accept? (Y/N): ")
    students.remove(navigator)

accept = "n"
while accept.lower() == 'n':
    operator = choose_random_student(students)
    accept = input(f"The operator chosen is : {operator}. Accept? (Y/N): ")
    students.remove(operator)

print(f"Navigator: {navigator}")
print(f"Operator: {operator}")


