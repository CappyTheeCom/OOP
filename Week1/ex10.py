class Enrollment:

    def __init__(self, code, credit, status):
        self.code = code 
        self.credit = credit 
        self.status = status

    def print_enrol(self):
        info = "Course Information: " + self.code + ", Credits: " + self.credit + ", Status: " + self.status
        return info


course_code = "DPIT121"
course_credit = str(4)
course_status = "Enrolled"

student_enrol = Enrollment(course_code,course_credit,course_code)
print(student_enrol.print_enrol())


