class Dec:

    def __init__(self,fnum,snum):
        self.fnum = fnum
        self.snum = snum 
    
    def calc(self):
        try:
            product = self.fnum / self.snum
            return print(f"{product:.2f}")
        except ZeroDivisionError:
            print("Error: can not be divided by zero")
        


first_num = float(input("Enter a first integer: "))
second_num = float(input("Enter a second integer: "))

numb = Dec(first_num, second_num)

numb.calc()