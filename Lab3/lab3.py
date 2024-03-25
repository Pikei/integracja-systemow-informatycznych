import sqlite3
import time
import Lab3.create_tables as create
import Lab3.add_values as add
import Lab3.actions as actions


def start():
    try:
        create.tables()
        print("Created database.")
        time.sleep(1)
        print("Added values to tables.")
        add.values()
        time.sleep(1)
        choice()
    except sqlite3.OperationalError:
        choice()


def choice():
    print("Choose query option:")
    print("1. Print all students")
    print("2. Print all students from one group")
    print("3. Print all students, that have grade higher or equal to chosen grade")
    print("4. Print all lecturers and their subjects")
    print("5. Print department and all of its student groups")
    print("6. Print all students and their average grade")
    match (input("Your choice: ")):
        case "1":
            actions.print_all_students()
        case "2":
            actions.print_students_from_group()
        case "3":
            actions.print_students_with_grade_higher_or_equal_to_grade()
        case "4":
            actions.print_lecturers_and_their_subjects()
        case "5":
            actions.print_departments()
        case "6":
            actions.print_avg_grade()
        case _:
            print("\nWrong option!\n")
            time.sleep(1)
            choice()


