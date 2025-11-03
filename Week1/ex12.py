class grade:

    def __init__(self, name, age, gpa):
        self.name = name 
        self.age = age
        self.gpa = gpa

    def print_statement(self):
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"GPA: {gpa:.2f}")



name = input("Enter name: ")
age = (input("Enter age: "))
gpa = float(input("Enter GPA: "))

student = grade(name, age, gpa)
student.print_statement()