import random

#Creating a player based class
class Player: 
    def __init__(self,name,race,age):
        self.__age = age 
        self.__name = name 
        self._race = race
        self._hp = 100
        self._mp = 100 
        self._sp = 100
        self.__playableRace = ["human","dwarf","elf","tiefling","half-elf","orc"]
    
    #Checking for the player health, stamania and mana 
    def playerHealth(self):
         return self._hp
    
    def playerStamania(self):
         return self._sp
    
    def playerMagic(self):
         return self._mp
    
    #Creating a playable race
    def playAbleRace(self):

        if self._race in self.__playableRace:
                return f"You have selected to play as {self._race}"
        else:
             return "please select an playable race!!!"
        
    #Creating appropiate ages for relevant races 
    def playAbleAge(self):
         
         #choosing within elfs and dwarfs
         if self._race in ["elf","half-elf","dwarf","orc"]:
              if 30 <= self.__age <= 820:
                   return f"Your age is {self.__age}"
              else:
                   return "Please select a proper age range!!"
         #Orcs and tieflings share the same age range
         elif self._race in ["tiefling, orc"]:
              if 30 <= self.__age <= 500:
                   return f"Your age is {self.__age}"
              else:
                   return "Please select a proper age!!"
         #Humans will have typical age ranges
         elif self._race in ["human"]:
            if 19 <= self.__age <= 80:
                 return f"Your age is {self.__age}"
            else:
                 return "Please enter a proper age range"
   
    #Allocating player health        
    def playerBonusStats(self):
         if self._race in ["dwarf, orc"]:
              self._hp += 30
              return f"Your current hp with race bonus: {self._hp}"
         elif self._race in ["elf,half-elf,tiefling"]:
              self._mp += 30 
              return f"Your current mp with race bonus: {self._mp}"
         elif self._race in {"human"}:
              self._hp += 10
              self._mp += 10 
              self._sp += 10 
              return f"Your race bonus is +10 across all stats!"
    
    #Creating player name
    def selectPlayerName(self):
        if len(self.__name) <= 4:
             return "Please enter a name with atleasat four characters!"
        elif self.__name in ["!","@","#","$","%","^","&","*","+","="]:
             return "Your name must not have any characters!!!"
        else:
             return f"Your name is {self.__name}"
        
    #Creating player damage
    def playerDamge(self,damage):
         currentPlayerHp = self._hp - damage 
         return currentPlayerHp
    
    def playerHeal(self, potion):
         currentPlayerHp = self._hp + potion
         return currentPlayerHp
         
         


#creating class archetypes 
class PlayerClass(Player):
     #Inheriting the relevant attributes to the class type
     def __init__(self,race,age, health,magick,stamania,className):
          super.__init__(self, race,age,health,magick,stamania)
          self.__class = className 
          self.__classType = ["warrior,rogue,mage"]
          self._dp = 0

     #Creating getter variable for defense points 
     def getPlayerDp(self):
         return self._dp 
        
    #creating different class attributes 
     def classAttributes(self):
          if self.__class in self.__classType:
               if self.__class == "warrior":
                    self._hp += 50 
                    self._mp -= 30
                    self._sp += 10
                    self._dp += 15
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
               elif self.__class == "rogue":
                    self._hp -= 10 
                    self._mp += 15 
                    self._sp += 50 
                    self._dp += 10
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
               elif self.__class == "mage":
                    self._hp -= 20 
                    self._mp += 50 
                    self._sp += 15
                    self._dp += 5
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
          else:
               return "Input a proper class!!!"
          
                   
#Craeitng weapon template
class Weapon:
     #Using player as a way to pass the method through the class
     def __init__(self, player):
          self._player = player
          self._weaponAtk = 0
          self._lightWeapons = ["quarter-staff, short-sword, dagger, long-sword, mace, buckle, crossbow"]
          self._heavyWeapons = ["great-sword, great-hammer, great-mace, bow, club"]
          self._magicWeapons = ["tome, spells, staff, runes"]

     #Creating Weapon focuses for particular classes         
     def weaponStart(self):

          #Heavy weapon profieceny 
          if self._player._hp >= 130:
               for weapons in self._heavyWeapons:
                    weapons 
               return f"Please select a starting weapon"
          #light weapon profieceny
          if self._player._sp >= 130:
               for weapons in self._lightWeapons:
                    weapons 
               return f"Please select a starting weapon"
          #magic profieceny 
          if self._player._mp >= 130:
               for weapons in self._magicWeapons:
                    weapons 
               return f"Please select a starting weapon"
          
     #Creating weapon attack damage 
     def weaponDmg(self, weapon):
          #Checking if the player profiecent in health
          if weapon in self._heavyWeapons:
               self._atk = 10
               for damage in range (self._player._hp+2, 130):
                    self._weaponAtk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self._weaponAtk <= 0:
                         self._weaponAtk -= 5
                         return f"You are not profiecent to use a {weapon}: -5 Attack!!"
               return f"Your {weapon} does {self._weaponAtk}!"
          
          #checking for stamania profieceny 
          elif weapon in self._lightWeapons:
               self._atk = 10
               for damage in range (self._player._sp+2, 130):
                    self._atk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self._weaponAtk <= 0:
                         self._weaponAtk -= 5
                         return f"You are not profiecent to use a {weapon}: -5 Attack!!"
               return f"Your {weapon} does {self._atk}!"
          
          #Checking if the player profiecent in magic damage 
          elif weapon in self._magicWeapons:
               self._atk = 10
               for damage in range (self._player._mp+2, 130):
                    self._weaponAtk += damage 
                    #If the range is 0 (or some how less) it reduces attack damage
                    if self._atk <= 0:
                         self._weaponAtk -= 5
                         return f"You are not profiecent to use a {weapon}: -5 Attack!!"
               return f"Your {weapon} does {self._weaponAtk}!"
          else:
               return f"There no weapon equipped!!!"


#Creating light weapon profieceny and skills
class LightWeapons(Weapon):
     #Creating the weapon dictonary to allow for dynamically adding 
     weaponTypes = {}

     def adding_weapons(self):
          for weapons in self._lightWeapons:
               LightWeapons.weaponTypes[weapons] = 0
          return 

     #adding incremental weapon profieceny 
     def weaponProfieceny(self):
          selectWeapon = input("Please select a weapon to add profieceny into: ")
          #Checking if the weapon within the light weapon types
          if selectWeapon in LightWeapons.weaponTypes:
               LightWeapons.weaponTypes[selectWeapon] += 5
               return f"{selectWeapon} current profieceny: {LightWeapons.weaponTypes[selectWeapon]}"
          else:
               return "Please select a proper weapon!!"


#Creating heavy weapon profieceny and skills
class HeavyWeapons(Weapon):
     #Creating the weapon dictonary to allow for dynamically adding 
     weaponTypes = {}
     def adding_weapons(self):
          for weapons in self._heavyWeapons:
               HeavyWeapons.weaponTypes[weapons] = 0
          return 

     #adding incremental weapon profieceny 
     def weaponProfieceny(self):
          selectWeapon = input("Please select a weapon to add profieceny into: ")

          #Checking if the weapon within the light weapon types
          if selectWeapon in HeavyWeapons.weaponTypes:
               HeavyWeapons.weaponTypes[selectWeapon] += 5
               return f"{selectWeapon} current profieceny: {HeavyWeapons.weaponTypes[selectWeapon]}"
          else:
               return "Please select a proper weapon!!"
          

#Creating light weapon profieceny and skills
class MagicWeapons(Weapon):
     #Creating the weapon dictonary to allow for dynamically adding 
     weaponTypes = {}
     def adding_weapons(self):
          for weapons in self._magicWeapons:
               MagicWeapons.weaponTypes[weapons] = 0
          return 

     #adding incremental weapon profieceny 
     def weaponProfieceny(self):
          selectWeapon = input("Please select a weapon to add profieceny into: ")

          #Checking if the weapon within the light weapon types
          if selectWeapon in MagicWeapons.weaponTypes:
               MagicWeapons.weaponTypes[selectWeapon] += 5
               return f"{selectWeapon} current profieceny: {MagicWeapons.weaponTypes[selectWeapon]}"
          else:
               return "Please select a proper weapon!!"
          
     

          

     
          

          


          

                    

     

    

        
        
              
         
         
            

    
              