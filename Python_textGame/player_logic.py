import random
#Creating a player based class
class Player: 
    def __init__(self,name,race,age):
        self._age = age 
        self._name = name 
        self._race = race
        self._hp = 25
        self._mp = 25 
        self._sp = 25
        self.__playableRace = ["human","dwarf","elf","tiefling","half-elf","orc"]
    
    #Checking for the player health, stamania and mana 
    def getplayerHealth(self):
         return self._hp
    
    def getplayerStamania(self):
         return self._sp
    
    def getplayerMagic(self):
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
         elif self._race in ["tiefling", "orc"]:
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
         if self._race in ["dwarf","orc"]:
              self._hp += 30
              return f"Your current hp with race bonus: {self._hp}"
         elif self._race in ["elf","half-elf","tiefling"]:
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
    
    def playerHeal(self, potion):
         self._hp += potion
         return self._hp
         
         


#creating class archetypes 
class PlayerClass(Player):
     #Inheriting the relevant attributes to the class type
     def __init__(self,name,race,age,className):
          super().__init__(name,race,age)
          self.__class = className
          self._weaponAttributes = {"Strength" : 10,
                                    "Intelligence": 10, 
                                    "Dexterity": 10}  
          self.__classType = ["warrior","rogue","mage"]
          self._dp = 0

     #Creating getter variable for defense points 
     def getPlayerDp(self):
         return self._dp 
        
    #creating different class attributes 
     def classAttributes(self):
          if self.__class in self.__classType:
               if self.__class == "warrior":
                    self._hp += 10 
                    self._mp -= 7
                    self._sp += 10
                    self._dp += 10
                    self._weaponAttributes["Strength"] += 8
                    self._weaponAttributes["Intelligence"] -= 2
                    self._weaponAttributes["Dexterity"] += 2
                    return f"Your {self.__class} attributes are: hp:{self._hp:<15} sp:{self._sp:<15} mp:{self._mp:<15} "
               elif self.__class == "rogue":
                    self._hp -= 5 
                    self._mp += 5 
                    self._sp += 10 
                    self._dp += 7
                    self._weaponAttributes["Strength"] += 2
                    self._weaponAttributes["Intelligence"] += 2
                    self._weaponAttributes["Dexterity"] += 6
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<20} mp{self._mp:^10} "
               elif self.__class == "mage":
                    self._hp -= 10 
                    self._mp += 10 
                    self._sp += 7
                    self._dp += 5
                    self._weaponAttributes["Strength"] -= 2
                    self._weaponAttributes["Intelligence"] += 8
                    self._weaponAttributes["Dexterity"] += 2
                    return f"Your {self.__class} attributes are: hp{self._hp:<15} sp{self._sp:<16} mp{self._mp:<17} "
          else:
               return "Input a proper class!!!"
          
     def playerDeathState(self):
         rollChance =  random.randint(0,20)
         saveRolls = 0 
         deathRolls = 0 

         if self._hp < 0: 
              print(f"{self._name} has entered a dying state!!!")
          
              while True:
                    #Creating save and death rolls
                    if rollChance > 10:
                         saveRolls += 1 
                         print(f"You have {saveRolls}/3 left to revive")
                    else:
                         deathRolls += 1 
                         print(f"You have {deathRolls}/3 left before death")
                    
                    #Checking if either critera is fulfilled
                    if saveRolls == 3:
                         self._hp = 20 + self._dp
                         print(f"{self._name} have succeeded the save rolls HP: {self._hp}")
                         return False
                    elif deathRolls == 3:
                         print(f"{self._name} has died, game over!!")
                         return True
         else:
              pass 
     
     #Allowing the player to check current stats to see reasources
     def checkingPlayerStats(self):
          return f"Your current stats: hp:{self._hp:<15} sp:{self._sp:<16} mp:{self._mp}"


                   
#Craeitng weapon template
class Weapon:
     #Using player as a way to pass the method through the class
     def __init__(self, player):
          self._player = player
          self._weaponModifier = 0
          self._minDamage = 0
          self._maxDamage = 0
          self._lightWeapons = ["quarter-staff", "short-sword", "dagger", "long-sword", "mace", "buckle", "crossbow"]
          self._heavyWeapons = ["great-sword", "great-hammer", "great-mace", "bow", "club"]
          self._magicWeapons = ["tome", "spells", "staff", "runes"]

     #Creating Weapon focuses for particular classes         
     def weaponStart(self):

          #Heavy weapon profieceny 
          if self._player._hp >= 130:
               print("Heavy weapons available: ", end='')
               for weapons in self._heavyWeapons:
                    print(weapons, end=' ') 
               return 
          #light weapon profieceny
          if self._player._sp >= 130:
               print("Light weapons available: ", end='')
               for weapons in self._lightWeapons:
                    print(weapons, end=' ') 
               return 
          #magic profieceny 
          print("Magic weapons available: ", end='')
          if self._player._mp >= 130:
               for weapons in self._magicWeapons:
                    print(weapons, end=' ') 
               return 
          
     #Creating weapon attack damage 
     def weaponDmgCheck(self, weapon):
          #Checking if the player profiecent in health
          if weapon in self._heavyWeapons:
               #Getting the strength modifier
               strengthModify = self._player._weaponAttributes.get("Strength")
               self._weaponModifier = (strengthModify - 10) // 2
               self._minDamage = 0 + self._weaponModifier
               self._maxDamage = 10 + self._weaponModifier               
               return f"Your {weapon} does {self._minDamage}-{self._maxDamage}!"
          
          #checking for stamania profieceny 
          elif weapon in self._lightWeapons:
               dexModify = self._player._weaponAttributes.get("Dexterity")
               self._weaponModifier = (dexModify - 10) // 2
               self._minDamage = 2 + self._weaponModifier
               self._maxDamage = 8 + self._weaponModifier  
               return f"Your {weapon} does {self._minDamage}-{self._maxDamage}!"
          
          #Checking if the player profiecent in magic damage 
          elif weapon in self._magicWeapons:
               intModify = self._player._weaponAttributes.get("Intelligence")
               self._weaponModifier = (intModify - 10) // 2
               self._minDamage = 2 + self._weaponModifier
               self._maxDamage = 8 + self._weaponModifier  
               return f"Your {weapon} does {self._minDamage}-{self._maxDamage}!"
          else:
               return f"There no weapon equipped!!!"
     
     #Getting weapon stat 
     def getWeaponAtk(self):
          weaponDmg = random.randint(self._minDamage, self._maxDamage)
          return weaponDmg


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
          
     

          

     
          

          


          

                    

     

    

        
        
              
         
         
            

    
              