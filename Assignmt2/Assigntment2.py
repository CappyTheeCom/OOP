#Defines the australian user and methods associated with the class.
class AustralianUser:

    def __init__(self,age,gender):
        self._age = age 
        self._gender = gender 

    #Vegetabke intake function 
    def veg_intake(self):

        if 19<= self._age <=50:
            return "Your recommended vegetable intake 6 servings"
        elif 51<= self._age <= 70:
            return "Your recommended vegetable intake 5.5 servings"
        elif 71<= self._age:
            return "Your recommended vegetable intake 5 servings"
    
    #Fruit intake function 
    def fruit_intake(self):

        if 19<= self._age:
            return "Your recommended fruit intake 2 servings"
    
    #Grain intake function 
    def grain_intake(self):

        if 19<= self._age <=50:
            return "Your recommended grain intake 6 servings"
        elif 51<= self._age <= 70:
            return "Your recommended grain intake 6 servings"
        elif 71<= self._age:
            return "Your recommended grain intake 4.5 servings"
    
    #Meat intake function 
    def meat_intake(self):

        if 19<= self._age <=50:
            return "Your recommended meat intake 3 servings"
        else:
            return "Your recommended meat intake 2.5 servings"
        
    #Dairy intake method
    def dairy_intake(self):

        if 19<= self._age <=50:
            return "Your recommended dairy intake 2.5 servings"
        elif 51<= self._age <= 70:
            return "Your recommended dairy intake 2.5 servings"
        elif 71<= self._age:
            return "Your recommended dairy intake 3.5 servings"
    
    #Makes the food statement into an tuple so it can be printed out 
    def printstatement_food(self):
        file_name = input("Enter file-name: ")

        file_name+="_dietary_requirements.txt"

        output = (
            f"{self.dairy_intake()}\n"
            f"{self.fruit_intake()}\n"
            f"{self.grain_intake()}\n"
            f"{self.meat_intake()}\n"
            f"{self.veg_intake()}\n"
            f"{self.__str__()}"
        )
        with open(file_name, "a") as f:
            f.write(output)
        
        return(f"Results saved to {file_name}")
            
        

    #string method to display current serving sizes 
    def __str__(self):
                return ("A single serve of vegetables is 75g (100-350kj)\n"
                "A single serve of fruit 150g(350kj)\n"
                "A single serve of grains is (500kj)\n"
                "A single serve of meat is (500-600kj)\n"
                "A single serve of dairy is (500-600kj)\n")
    
#Allow for the creation of another class to allow for further additions into Males if additional information is provided
class MaleUser(AustralianUser):
    pass

#Adds additional attributes related to women 
class FemaleUser(AustralianUser):
    
    def __init__(self,age,gender,pregnant,bFeeding):
        super().__init__(age,gender)
        self.__pregnant = pregnant
        self.__bFeeding = bFeeding
    
    #Redefine's the vegetable function to take into account for pregnant women 
    def veg_intake(self):
        if self.__bFeeding == True:
            return "Your recommended vegetable intake 7.5 servings"
        else:
            return "Your recommended vegetable intake 5 servings"
    
    #Inherits fruit function from australian base class 
    def fruit_intake(self):
        return super().fruit_intake()
    
    #Redefines meat intake to account pregnancy 
    def meat_intake(self):
        if self.__pregnant == True:
            return "Your recommended meat intake 3.5 servings"
        elif 19<= self._age <= 50:
            return "Your recommended meat intake 2.5 servings"
        else:
            return "Your recommended meat intake 2 servings"

    #Different variables for women dairy intake
    def dairy_intake(self):
        if 19<= self._age <= 50:
            return "Your recommended dairy intake 2.5 servings"
        else:
            return "Your recommended dairy intake 4 servings"

    #Different variables for women grain intake  
    def grain_intake(self):
        if 19<= self._age <=50:
            return "Your recommended grain intake 2.5 servings"
        elif 51<= self._age <= 70:
            return "Your recommended grain intake 2.5 servings"
        elif 71<= self._age:
            return "Your recommended grain intake 3.5 servings"
    
    def __str__(self):
        return super().__str__()
        


class Under18User(AustralianUser):

    def __init__(self,age,gender):
        super().__init__(age,gender)

    #Vegetable intake for under 18's
    def veg_intake(self):
        if  2<= self._age <=3:
            return "Your recommended vegetable intake 2.5 servings"
        elif 4<= self._age <=8:
            return "Your recommended vegetable intake 4.5 servings"
        elif 9<= self._age <= 11:
            return "Your recommended vegetable intake 5 servings"
        
        #Checks for gender as they differenate at 12+
        elif self._gender == "male" or self._gender == "Male":
            if 12<= self._age <=18:
                return "Your recommended vegetable intake 5.5 servings"
        else:
            return "Your recommended vegetable intake 5 servings"

    #Fruit intake for under18's    
    def fruit_intake(self):
        if  2<= self._age <=3:
            return "Your recommended fruit intake 1 servings"
        elif 4<= self._age <=8:
            return "Your recommended fruit intake 1.5 servings"
        elif 9<= self._age <= 18:
            return "Your recommended fruit intake 2 servings"
        
    def grain_intake(self):
        if  2<= self._age <=8:
            return "Your recommended grain intake 4 servings"
        #Checks if the user is male
        if self._gender == "male" or self._gender == "Male":
            if 9<= self._age <=11:
                return "Your recommended grain intake 5 servings"
            elif 12<= self._age <=13:
                return "Your recommended grain intake 6 servings"
            elif 14<= self._age <=18:
                return "Your recommended grain intake 7 servings"
            
            
        #Continues if female
        else:
            if 9<= self._age <=11:
                return "Your recommended grain intake 4 servings"
            elif 12<= self._age <=13:
                return "Your recommended grain intake 5 servings"
            elif 14<= self._age <=18:
                return "Your recommended grain intake 7 servings"
        
    def meat_intake(self):
        #Uses the same intake regardless of gender 
        if  2<= self._age <=3:
            return "Your recommended meat intake 1 servings"
        elif 4<= self._age <=8:
            return "Your recommended meat intake 1.5 servings"
        elif 9<= self._age <= 18:
            return "Your recommended meat intake 2.5 servings"
    
    #Checks for recommeneded dairy intake 
    def dairy_intake(self):
        #Checks for the inital age between both genders
        if 2 <= self._age <= 3:
            return "Your recommended dairy intake 1.5"
        #Does a check if the gender is male since gender deviates
        if self._gender == "male" or self._gender == "Male":
            if 4 <= self._age <= 8:
                return "Your recommended dairy intake 2 servings"
            elif 9 <= self._age <= 11:
                return "Your recommended dairy intake 2.5 servings"
            elif 12 <= self._age <= 18:
                return "Your recommended dairy intake 3.5 servings"
    
        else:  # else the statement views them as female 
            if 4 <= self._age <= 8:
                return "Your recommended dairy intake 1.5 servings"
            elif 9 <= self._age <= 18:
                return "Your recommended dairy intake 3.5 servings"

    #Inherits the str method from the base class    
    def __str__(self):
        return super().__str__()

def main():
    #Checks for age input to be valid 
    try:
        age_input = int(input("Enter your age: "))
    except ValueError:
        print("Invalid Input, please enter a proper integer")
        return
    
    #Checks if gender input male or female as other not available 
    gender_input = input("Enter your gender(female/male): ")
    if gender_input not in ['male', 'female','Male','Female']:
        print("Please enter the given genders.")
        return

    #Checks for age input is less than 18 
    if age_input <=18:
        #Gender has no influence as pregnancy and breastfeeding does not account for those under 18
        minor_user = Under18User(age_input,gender_input)
        print(minor_user.dairy_intake())
        print(minor_user.fruit_intake())
        print(minor_user.grain_intake())
        print(minor_user.meat_intake())
        print(minor_user.veg_intake())
        print(str(minor_user))

        #Asks for file export
        file_export = input("Would you like to export the information(y/n)?: ")

        #Checks if input wanted does state whether they do want a file or not
        if file_export not in ['y','Y','n','N']:
            print("Please enter a proper input.")
        elif file_export == "y" or file_export == "Y":
            print(minor_user.printstatement_food())
        elif file_export == "n" or file_export == "N":
            pass

    #Checks if the user if a women and asks for breastfeeding and pregnancy 
    elif age_input > 18 and gender_input == "female" or gender_input == "Female":
        #Uses bool as an check box rather than yes or no for easier usuage 
        bFeeding_input = bool(input("Check if you're breastFeeding (leave empty if not): "))
        pregnant_input = bool(input("Check if you're pregnant(leave empty if not): "))
        #Uses female class and calls on the polymorphed functions
        female_user = FemaleUser(age_input,gender_input,bFeeding_input,pregnant_input)
        print(female_user.dairy_intake())
        print(female_user.fruit_intake())
        print(female_user.grain_intake())
        print(female_user.meat_intake())
        print(female_user.veg_intake())
        print(str(female_user))
        file_export = input("Would you like to export the information(y/n)?: ")
        #Does file exports from the response 
        if file_export not in ['y','Y','n','N']:
            print("Please enter a proper input.")
        elif file_export == "y" or file_export == "Y":
            print(female_user.printstatement_food())
        elif file_export == "n" or file_export == "N":
            pass

    else:
        #Assumes the user is a male and uses the parent class as the bases 
        male_user = MaleUser(age_input,gender_input)
        print(male_user.dairy_intake())
        print(male_user.fruit_intake())
        print(male_user.grain_intake())
        print(male_user.meat_intake())
        print(male_user.veg_intake())
        print(str(male_user))
        file_export = input("Would you like to export the information(y/n)?: ")
        #Does file exports
        if file_export not in ['y','Y','n','N']:
            print("Please enter a proper input.")
        elif file_export == "y" or file_export == "Y":
            print(male_user.printstatement_food())
        elif file_export == "n" or file_export == "N":
            pass
main()

