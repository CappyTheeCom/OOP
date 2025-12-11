#Creating a player based class
class player: 
    def __init__(self,name,race,age):
        self.__age = age 
        self.__name = name 
        self._race = race
        self._hp = 100
        self._mp = 100 
        self._sp = 100
        self.__playableRace = ["human","dwarf","elf","tiefling","half-elf","orc"]

    #Creating a playable race
    def playAbleRace(self):

        if self._race in self.__playableRace:
                return f"You have selected to play as {self._race}"
        else:
             return "please select an playable race!!!"
        
    #Creating appropiate ages for relevant races 
    def playAbleAge(self):
         
         #choosing within elfs and dwarfs
         if self.__race in ["elf","half-elf","dwarf","orc"]:
              if 30 <= self.__age <= 820:
                   return f"Your age is {self.__age}"
              else:
                   return "Please select a proper age range!!"
         #Orcs and tieflings share the same age range
         elif self.__race in ["tiefling, orc"]:
              if 30 <= self.__age <= 500:
                   return f"Your age is {self.__age}"
              else:
                   return "Please select a proper age!!"
         #Humans will have typical age ranges
         elif self.__race in ["human"]:
            if 19 <= self.__age <= 80:
                 return f"Your age is {self.__age}"
            else:
                 return "Please enter a proper age range"
   
    #Allocating player health        
    def playerBonusStats(self):
         if self.__race in ["dwarf, orc"]:
              int(self._hp) += 30
              return f"Your current hp with race bonus: {self._hp}"
         elif self.__race in ["elf,half-elf,tiefling"]:
              int(self._mp) += 30 
              return f"Your current mp with race bonus: {self._mp}"
         elif self.__race in {"human"}:
              int(self._hp) += 10
              int(self._mp) += 10 
              int(self._sp) += 10 
              return f"Your race bonus is +10 across all stats!"
         
         
    #Displaying playable races
    def displayRaces(self):
        for race in self.__playableRace:
             race
        self._race = input("Please select a race: ")
        return 
    #Creating player name
    def selectPlayerName(self):
        self.__name = input("Please enter a name: ")

        if len(self.__name) <= 4:
             return "Please enter a name with atleasat four characters!"
        elif self.__name in ["!,@,#,$,%,^,&,*,+,="]:
             return "Your name must not have any characters!!!"
        else:
             return f"Your name is {self.__name}"
    
#creating class archetypes 
class PlayerClass(player):
     #Inheriting the relevant attributes to the class type
     def __init__(self,race,health,magick,stamania,className):
          super.__init__(self, race,health,magick,stamania)
          self.__class = className 
          self.__classType = ["warrior,rogue,mage"]

    #creating different class attributes 
     def classAttributes(self):
          if self.__class in self.__classType:
               if self.__class == "warrior":
                    self._hp += 50 
                    self._mp -= 30
                    self._sp += 10
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
               elif self.__class == "rogue":
                    self._hp -= 10 
                    self._mp += 15 
                    self._sp += 50 
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
               elif self.__class == "mage":
                    self._hp -= 20 
                    self._mp += 50 
                    self._sp += 15 
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
          else:
               return "Input a proper class!!!"
    


#Craeitng weapon template
class Weapon(player):
     def __init__(self, equiped):
          self.__equip = equiped 
          self.__atk = 0
          self._prof = 0 
          self.__lightWeapons = ["quarter-staff, short-sword, dagger, long-sword, mace, buckle, crossbow"]
          self.__heavyWeapons = ["great-sword, great-hammer, great-mace, bow, club"]
          self.__magicWeapons = ["tome, spells, staff, runes"]

     #Creating Weapon focuses for particular classes         
     def weaponProficency(self):

          #Heavy weapon profieceny 
          if self._hp >= 130:
               for weapons in self.__heavyWeapons:
                    weapons 
               return f"Please select a starting weapon"
          #light weapon profieceny
          if self._sp >= 130:
               for weapons in self.__lightWeapons:
                    weapons 
               return f"Please select a starting weapon"
          #magic profieceny 
          if self._mp >= 130:
               for weapons in self.__magicWeapons:
                    weapons 
               return f"Please select a starting weapon"
          
     #Creating weapon attack damage 
     def weaponDmg(self):
          #Checking if the player profiecent in health
          if self.__equip in self.__heavyWeapons:
               self.__atk = 10
               for damage in range (self._hp+2, 130):
                    self.__atk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self.__atk <= 0:
                         self._atk -= 5
                         return f"You are not profiecent to use a {self.__equip}: -5 Attack!!"
               return f"Your {self.__equip} does {self.__atk}!"
          
          #checking for stamania profieceny 
          elif self.__equip in self.__lightWeapons:
               self.__atk = 10
               for damage in range (self._sp+2, 130):
                    self.__atk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self.__atk <= 0:
                         self._atk -= 5
                         return f"You are not profiecent to use a {self.__equip}: -5 Attack!!"
               return f"Your {self.__equip} does {self.__atk}!"
          
          #Checking if the player profiecent in magic damage 
          elif self.__equip in self.__magicWeapons:
               self.__atk = 10
               for damage in range (self._mp+2, 130):
                    self.__atk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self.__atk <= 0:
                         self._atk -= 5
                         return f"You are not profiecent to use a {self.__equip}: -5 Attack!!"
               return f"Your {self.__equip} does {self.__atk}!"

          else:
               return f"There no weapon equipped!!!"
          


          


          
          
          

                    

     

    

        
        
              
         
         
            

    
              