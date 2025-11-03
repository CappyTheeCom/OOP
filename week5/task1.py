class Address:

    def __init__(self,streetNum,streetName,city,state,postCode,country):
        self.__num = streetNum 
        self.__name = streetName 
        self.__city = city 
        self.__state = state
        self.__post = postCode
        self.__country = country 


class Staff:
    staff_list = []

    def __init__(self,fname,lname,dob,address,mobileNum,staffId):
        self._fname = fname 
        self._lname = lname 
        self._dob = dob 
        self._address = address
        self._mobile = mobileNum
        self._staffId = staffId
    
    
    def add_staff(self):
        #Creating staff address
        staff_streetNum = int(input("Enter your street number: "))
        staff_streetName = input("Enter your street Name: ")
        staff_city = input("Enter staff city: ")
        staff_state = input("Enter your state: ")
        staff_post = int(input("Enter your post-code: "))
        staff_country = input("Enter your country: ")


        #creating staff informtation 
        staff_fname = input("Enter your firstname: ")
        staff_lname = input("Enter your lastname: ")
        staff_dob = input("Enter your date of birth: ")
        staff_address = Address(staff_streetNum,staff_streetName,staff_city,staff_state,staff_post,staff_country)
        staff_mobile = int(input("Enter your mobile number: "))
        staff_id = int(input("Enter your ID: "))



        new_staff = Staff(staff_fname,staff_lname,staff_dob,staff_address,staff_mobile,staff_id)

        Staff.staff_list.append(new_staff)

        return new_staff
    

    @classmethod
    def search_staff(cls):
        console_id = int(input("Enter staff member id: "))

        for ident in cls.staff_list:
            if ident._staffId == console_id:
                return ident 
            
        return "staff does not exist!"
    
    @classmethod
    def delete_staff(cls):
        console_id = int(input("Enter staff member id: "))

        for ident in cls.staff_list:
            if ident._staffId == console_id:
                
                Staff.staff_list.remove(ident)
                return "Staff has been removed!"
            
        return "staff does not exist!"
        
