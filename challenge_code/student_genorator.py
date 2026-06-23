from Challenge_Six import Students

'''
function to return a list of student objects
input:none
output: list of student objects
'''

def load_students():

    data_file = open("students.csv", "r")
    
    students = []

    for line in data_file:
        try:
            student_info = line.split(",")
            student = Students(student_info[0],student_info[1], student_info[2], int(student_info[3]), float(student_info[4]),student_info[5])
            print(student)
        except:
            print("Invalid line")
            continue
        
        students.append(student)
        
    data_file.close()

    return students

"""
function to get student dicts
input:none
output:a list of student dicts
"""
'''
function to conver student objects into student dicts
input: list of student objects
output:list of student dicts
'''
def student_to_dicts(list_of_students:list[Students]) -> list[dict]:
    #create an empty list to store the dict
    studnet_dict_list = []
    for student in list_of_students:
        student_dict = {}
        student_dict["first"] = student.get_first()
        student_dict["last"] = student.get_last()
        student_dict["major"] = student.get_major()
        student_dict["gpa"] = student.get_gpa()
        student_dict["class"] = student.get_class_level()
        student_dict["id"] = student.get_id()

        studnet_dict_list.append(student_dict)

    return studnet_dict_list
    #loop through the list and write each students data to a dict
        #create an empty dict
        #make entries into the dict using the student properties
        #first,last, major, gpa, class, id
        #append the dict to the list of dict
    #return list of dicts


def get_student_dicts():
    #get a list of students
    student_list = load_students()

    student_dicts = student_to_dicts(student_list)

    return student_dicts
