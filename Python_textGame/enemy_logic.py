import random

#Making enemy template
class Enemy:
     def __init__(self, name):
          self._enemyHp = 25 
          self._enemyDp = 10 
          self._atk = 240 
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
     
     #Enemy gold drop chance
     def enemyGold(self):
          if self._enemyHp <= 0:
               enemyDrop = 50 # will change back into proper rng gold output
               print(f"Enemy dropped {enemyDrop} Gold!")
               return enemyDrop
          

     #Creating enemy hit chances      
     def hitEnemy(self,playerDmg):
          currentHp = self._enemyHp - playerDmg
          return currentHp

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
     
     #Adding different classes to improve dealt damage from enemies
     def classAttributes(self):
               enemyClass = random.choice(self._classes)
               if enemyClass == "warrior":
                    self._hp += 10 
                    self._mp -= 7
                    self._sp += 10
                    self._dp += 10
                    self._weaponAttributes["Strength"] += 8
                    self._weaponAttributes["Intelligence"] -= 2
                    self._weaponAttributes["Dexterity"] += 2
                    return 
               elif enemyClass == "rogue":
                    self._hp -= 5 
                    self._mp += 5 
                    self._sp += 10 
                    self._dp += 7
                    self._weaponAttributes["Strength"] += 2
                    self._weaponAttributes["Intelligence"] += 2
                    self._weaponAttributes["Dexterity"] += 6
                    return
               elif enemyClass == "mage":
                    self._hp -= 10 
                    self._mp += 10 
                    self._sp += 7
                    self._dp += 5
                    self._weaponAttributes["Strength"] -= 2
                    self._weaponAttributes["Intelligence"] += 8
                    self._weaponAttributes["Dexterity"] += 2
                    return 
     
         
     def __str__(self):
          return "Bandit"


#Creating wolf enemy type               
class Wolf(Enemy):

     #Creating name
     def __init__(self, name=None):
          super().__init__(name)
          if self._name == None:
               self._name = "Wolf"
     
     #Creating wolf attack pattern 
     def wolfAtk(self):
          attack = random.randint(0,self._atk)
          return f"You have taken {attack}dmg"

     def __str__(self):
          return "Wolf"
