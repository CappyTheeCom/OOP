class solution:
    def __init__(self,fname,lname):
        self.fname =  fname 
        self.lname = lname 
    
    def print_statement(self):
        full_name = self.fname + " " + self.lname
        return print(f"Programming pioneer: {full_name}.")


user_info = solution("Ada","Lovelace")

user_info.print_statement()