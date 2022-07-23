import random
from student_list import students


def choose_random_student(students_list):
    student = random.choice(students_list)
    return student


def choose_acceptable_student(students_list):
    accept = "n"
    student = ""
    while accept.lower() == 'n':
        student = choose_random_student(students_list)
        accept = input(f"The student chosen is : {student}. Accept? (Y/N): ")
        students_list.remove(student)
    return student, students_list


navigator, updated_student_list = choose_acceptable_student(students)
operator, updated_student_list = choose_acceptable_student(updated_student_list)

print(f"Navigator: {navigator}")
print(f"Operator: {operator}")


