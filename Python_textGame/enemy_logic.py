import random

#Making enemy template
class Enemy:
     def __init__(self, name):
          self._enemyHp = 25 
          self._enemyDp = 10 
          self._atk = 4 
          self._name = name 
    
     #Creating enemy death state 
     def enemyDeathState(self):
          #creating save rolls
          saveState = 0 
          deathState = 0

          #Creating enemy death states
          if self._enemyHp <= 0:
               print(f"{self._name} is in dying state!!!")

          while True: 
               saveRoll = random.randint(0,20)

               #Creating condiitonal statement for the save state 
               if saveRoll >= 10:
                    saveState += 1 
                    print(f"{self._name} has achieved {saveState} saves!!")
               else:
                    deathState += 1
                    print(f"{self._name} has {deathState} death roll!!!")
               
               #Breaking the while loop if either state has been achieved 
               if saveState == 3:
                    self._enemyHp = 5 + self._enemyDp
                    print(f"The {self._name} returns to combat with {self._enemyHp}HP")
                    return False
               elif deathState == 3:
                    print(f"The {self._name} has died")
                    return True
     
          
     #Creating enemy hit chances      
     def hitEnemy(self,playerDmg):
          self._enemyHp -= playerDmg
          return self._enemyHp

     #Getting enemy stats
     def getEnemyHp(self):
          return self._enemyHp
     
     def getEnemyDF(self):
          return self._enemyDp
     
     def getEnemyAtk(self):
          return self._atk
     
#Creating bandit enemy type               
class Bandit(Enemy):

     #Creating name
     def __init__(self, name=None):
          super().__init__(name)
          if self._name == None:
               self._name = "Bandit"
               self._weaponAttributes = {"Strength" : 10,
                                         "Intelligence": 10, 
                                         "Dexterity": 10}
               self._classes = ["warrior","rogue","mage"]
               self._enemyClass = None
               self._minDam = 0
               self._maxDam = 0
     
     #Adding different classes to improve dealt damage from enemies
     def classAttributes(self):
               self._enemyClass = random.choice(self._classes)
               if self._enemyClass == "warrior":
                    self._name = "Bandit-Warrior"
                    self._enemyHp += 10 
                    self._enemyDp += 7
                    self._weaponAttributes["Strength"] += 8
                    self._weaponAttributes["Intelligence"] -= 2
                    self._weaponAttributes["Dexterity"] += 2
                    return 
               elif self._enemyClass == "rogue":
                    self._name = "Bandit-Rogue"
                    self._enemyHp -= 5 
                    self._enemyDp += 5
                    self._weaponAttributes["Strength"] += 2
                    self._weaponAttributes["Intelligence"] += 2
                    self._weaponAttributes["Dexterity"] += 6
                    return
               elif self._enemyClass == "mage":
                    self._name = "Bandit-Mage"
                    self._enemyHp -= 10 
                    self._enemyDp += 3
                    self._weaponAttributes["Strength"] -= 2
                    self._weaponAttributes["Intelligence"] += 8
                    self._weaponAttributes["Dexterity"] += 2
                    return 
     
     #Creating enemy attack modifier to be similar to the player attack modifier 
     def getEnemyAtk(self):
          if self._enemyClass == "warrior":
               abtMod = self._weaponAttributes.get("Strength")
               weaponMod = (abtMod - 10) // 2
               self._minDam = 0 + weaponMod
               self._maxDam = 10 + weaponMod
               self._atk = random.randint(self._minDam, self._maxDam)
               return self._atk
          elif self._enemyClass == "rogue":
               abtMod = self._weaponAttributes.get("Dexterity")
               weaponMod = (abtMod - 10) // 2
               self._minDam = 2 + weaponMod
               self._maxDam = 8 + weaponMod
               self._atk =  random.randint(self._minDam, self._maxDam)
               return self._atk
          elif self._enemyClass == "mage":
               abtMod = self._weaponAttributes.get("Intelligence")
               weaponMod = (abtMod - 10) // 2 
               self._minDam = 0 + abtMod
               self._maxDam = 12 + abtMod
               self._atk = random.randint(self._minDam, self._maxDam)
               return self._atk
          
     def __str__(self):

          if self._enemyClass == "warrior":
               return "Bandit-Warrior"
          elif self._enemyClass == "rogue":
               return "Bandit-Rogue"
          elif self._enemyClass == "mage":
               return "Bandit-Mage"
          
               

#Creating wolf enemy type               
class Wolf(Enemy):

     #Creating name
     def __init__(self, name=None):
          super().__init__(name)
          if self._name == None:
               self._name = "Wolf"
               self._atk = 10
     
     #Creating wolf attack pattern 
     def getEnemyAtk(self):
          self._atk = random.randint(0,self._atk)
          return self._atk
     
     #Creating a class string 
     def __str__(self):
          return "Wolf"
