class solution:
    
    def __init__(self):
        self.user_status = "active"
        self.login = 3 

    def data_type(self):
        return print(type(self.user_status),type(self.login)) 


user = solution()
user.data_type()