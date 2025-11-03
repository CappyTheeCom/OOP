class identification:

    def __init__(self, fname,lname,id):
        self._fname = fname 
        self._lname = lname 
        self._id = id

#subject identification
class Subject:

    def __init__(self,name,code):
        self._name = name 
        self._code = code 

#creating a sub-class to identifiy students 
class Student(identification):

    def __init__(self,fname,lname,id):
        super().__init__(fname,lname,id)
        self.subjects = []

#Creating sub-class to identifiy teachers
class Teacher(identification):

    def __init__(self,fname,lname,id):
        super().__init__(fname,lname,id)


#Creating admin system to modify user selections
class Admin_system:

    def __init__(self):
        self.students = []
        self.teachers_subjects = {}

        
    
    #Enrollment for students into a particular course 
    def student_enrollment(self):
        
        #Checks for details for an student
        fname = input("Enter your firstname: ")
        lname = input("Ënter your last name: ")
        ident = int(input("Enter your student identification: "))
        
        #Creaates a while loop to allow for additional students to part-take
        student = Student(fname,lname,ident)
        while True:
            
            subject_code = int(input("Enter course code: "))
            if subject_code == 0:
                break
            subject_name = input("Enter course name: ")
            if subject_name == "0":
                break
            
            subject_choice = Subject(subject_name,subject_code)
            student.subjects.append(subject_choice)
        
        #appends the subject choices and prints what they are enrolled with
        self.students.append(student)
        return print(f"Student {fname} {lname} enrolled with {len(student.subjects)} subjects")


    #Teacher enrollment into subjects
    def teacher_enrollment(self):


        fname = input("Enter your firstname: ")
        lname = input("Ënter your last name: ")
        ident = int(input("Enter your Teacher identification: "))
        
        teacher = Teacher(fname,lname,ident)

        while True:
            #Breaks the loop from user input
            subject_code = int(input("Enter course code: "))
            if subject_code == 0:
                break
            #breaks the loop from user input
            subject_name = input("Enter course name: ")
            if subject_name == "0":
                break
            #Checks for if a teacher already within the subject course 
            if subject_code in self.teachers_subjects:
                assigned_teacher = self.teachers_subjects[subject_code]
                print(f"Subject is already assigned to {assigned_teacher}")
                continue
        
        self.teachers_subjects[subject_code] = teacher 
        return print(f"Subject {subject_name} been assigned to {teacher._fname} {teacher._lname}")
    
    def student_reassignment(self):

        ident = int(input("Enter student identification number: "))

        for student in self.students:
            if ident == student.id:
                print("1) Add additional subjects\n" \
                "2) Remove a subjects\n" \
                "3) Exit the program")
                system_inp = int(input("Input an option"))
                if system_inp == 1:
                    


            else:
                print("Input a valid student id!")

    



#Main execution loop
def main():
    #Initalise class
    admin = Admin_system()
    #Continuious usage
    while True:
        #User access for the program
        user_input = int(input("Enter a number to access an option"))

        if user_input == 1:
            admin.student_enrollment()
        elif user_input == 2:
            admin.student_reassignment()
        else:
            print("Good-Bye")
            break


#execute relevant code
if __name__ == "__main__":
    main()







