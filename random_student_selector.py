# TODO Document with docstring for program
import datetime
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
            # TODO use sys.exit or raise custom exception
            print("No students left to choose in the student list")
            exit()
        accept = input(f"The student chosen is : {student}. Accept? (Y/N): ")
        students_list.remove(student)
    return student, students_list

# TODO function to log history


# TODO check for __main__
print("\nNow choosing navigator...")
navigator, updated_student_list = choose_acceptable_student(students)
print("Now choosing operator...\n")
operator, updated_student_list = choose_acceptable_student(updated_student_list)

# (datetime),navigator:(navigator),operator:(operator)
datetime_stamp = datetime.datetime.now()
with open("history.log", "a") as history_file:
    history_file.write(f"{datetime_stamp},NAVIGATOR:{navigator},OPERATOR:{operator}\n")
print(f"\nNavigator: {navigator}")
print(f"Operator: {operator}")


