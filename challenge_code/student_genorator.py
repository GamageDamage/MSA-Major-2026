from Challenge_Six import Students

def main():

    data_file = open("students.csv", "r")
    
    students = []

    for line in students:
        try:
            student_info = line.split(",")
            student = Students(student_info[0],student_info[1], student_info[2], int(student_info[3]), float(student_info[4]),  )