class Hobbies:

    def __init__(self, hob, hours):
        self.hob = hob 
        self.hours = hours

    def print_statement(self):
        hobby_dict = {
            "Hobby": self.hob,
            "Hours": self.hours
        }

        for key in hobby_dict:
            print(f'{key:<10}{":":>10} {hobby_dict[key]}')


hob = input("Enter your favourite hobby: ")
hours = int(input("Enter how many hours per week you spend on it? "))

hobbiest = Hobbies(hob, hours)
hobbiest.print_statement()