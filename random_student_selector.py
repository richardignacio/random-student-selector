#TODO Document with docstring for program
import random
try:
    from student_list import students
except ModuleNotFoundError as exc:
    print(f"Exception occurred: {exc}")
    print("Check the path of the student list file (student_list.py)")


def choose_random_student(students_list):
    # TODO Document with docstring for choose_random_student

    student = random.choice(students_list)
    return student


def choose_acceptable_student(students_list):
    # TODO Document with docstring for choose_acceptable_student

    accept = "n"
    student = ""
    while accept.lower() == 'n':
        try:
            student = choose_random_student(students_list)
        except IndexError:
            #TODO use sys.exit or raise custom exception
            print("No students left to choose in the student list")
            exit()
        accept = input(f"The student chosen is : {student}. Accept? (Y/N): ")
        students_list.remove(student)
    return student, students_list

#TODO function to log history

#TODO check for __main__
navigator, updated_student_list = choose_acceptable_student(students)
operator, updated_student_list = choose_acceptable_student(updated_student_list)

print(f"Navigator: {navigator}")
print(f"Operator: {operator}")


