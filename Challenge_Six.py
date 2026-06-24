class Students():
    def __init__(self,first,last, major,hours:int,gpa:float,id):
        self.__first = first
        self.__last = last
        self.__major = major
        self.__hours = hours
        self.__gpa = gpa
        self.__id = id

    def get_first(self):
        return self.__first
    
    def set_first(self,new_first:str):
        self.__first = new_first
    
    def get_last(self):
        return self.__last
    
    def set_last(self,new_last:str):
        self.__last = new_last
    
    def get_major(self):
        return self.__major
    
    def set_major(self,new_major:str):
        self.__major = new_major
    
    def get_hours(self):
        return self.__hours
    
    def set_hours(self,new_hours:int):
        self.__hours = new_hours

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self,new_gpa:float):
        self.__gpa = new_gpa
    
    def get_id(self):
        return self.__id

    def get_class_level(self):
        if 0 <= self.__hours <= 30:
            return "Freshman"
        elif 31<=self.__hours<=60:
            return "Sophomore"
        elif 61<=self.__hours<=90:
            return "Junior"
        elif 90<=self.__hours:
            return "Senior"
        
    def update_credit_hours(self,additional:int):
        self.__hours += additional
        return
    
    def print_student_data(self):
        print(f"{self.__first} {self.__last}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__id}")
