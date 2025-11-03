class time:

    def __init__(self, hours):
        self.hours = hours

    def calc(self):
        days = self.hours // 24
        remainder = self.hours % 24 
        return print(f"Total days:{days} and remaining hours: {remainder}")


hours_int = int(input("Enter total number of hours: "))

clock = time(hours_int)

clock.calc()