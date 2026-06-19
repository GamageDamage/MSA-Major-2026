from Challenge_Six import Students

def main():
    test_student = Students("Truman", "Tiger", "Mizzou Stuff", 1839, 4.5, "123456")
    test_student.print_student_data()

    test_student.set_hours(55)
    test_student.print_student_data()

main()