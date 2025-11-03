class solution:

    def __init__(self):
        self.fname = input("Enter your first name: ")
        self.fav = input("Enter your favourite programming language: ")
    
    def __str__(self):
        print(f"Hello,{self.fname}! you like {self.fav}")

user = solution()
user.__str__()