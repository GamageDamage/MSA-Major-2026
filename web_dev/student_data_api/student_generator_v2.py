from Student import Student
'''
Function to return a list of student objects
Input: none
Output: list of student objects
'''
def load_students() -> list[Student]:
    data_file = open("students.csv","r")
    students_list = []
    line_number = 0
    for line_of_data in data_file:
        line_number+=1
        if line_number == 1:
            continue
        student_info = line_of_data.split(",")
        print(line_of_data)
        if(len(student_info)!=6):
            print("ERROR: Invalid Format")
            continue    
        s_fname = student_info[0]
        s_lname = student_info[1]
        s_major = student_info[2]
        s_chours = student_info[3]
        s_gpa = student_info[4]
        s_ID = student_info[5]
        
        try:
            student: Student = Student(s_fname, s_lname, s_major, int(s_chours), float(s_gpa), s_ID.strip())
        except:
            print("Error: INVALID FORMATTING")
            continue
        s_Level = student.get_class_level()
        students_list.append(student)
    return students_list
'''
Function to convert student objects to student dictionaries
Input: list of student objects
Output: list of student dictionaries
'''
'''
Function to get student dictionaries
Input: None
Output: a list of student dictionaries
'''
def student_to_dictionary(list_of_students: list[Student])->list[dict]:
    #create an empty list to store the dcitionaries
    student_dictionary_list = []
    #loop through the list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        student_dictionary = {}
        #make entries into the dictionary using the student properties
        #firstname, last_name, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_ID()


        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    #return the list of dicitonaries
    return student_dictionary_list




def get_student_dictionaries():
    #get a list of students
    students_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(students_list)

    return student_dictionaries
