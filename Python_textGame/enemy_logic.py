import random
import player_logic

#Making enemy template
class Enemy:
     def __init__(self, name):
          self._enemyHp = 100 
          self._enemyDp = 10 
          self._atk = 15 
          self._name = name
    
     #Creating enemy defensive points
     def enemyDF(self,player):
          playerDmgRoll = random.randint(0,player._weaponAtk)

          if playerDmgRoll <= self._enemyDp:
               playerDmg = 0 
               return f"Player did {playerDmg}dmg to enemy!!!"
          elif playerDmgRoll > self._enemyDp:
               playerDmg = random.randint(0, player._weaponAtk) - self._enemyDp
               return f"Player did {playerDmg}dmg to enemy!!!"
          
     #Creating enemy death state 
     def enemyDeathState(self):
          #creating save rolls
          saveRoll = random.randint(0,20)
          saveState = 0 
          deathState = 0

          if self._enemyHp <= 0:
               print(f"{self._name} is in dying state!!!")

          while True: 

               #Creating condiitonal statement for the save state 
               if saveRoll >= self._enemyDp:
                    saveState += 1 
                    print(f"{self._name} has achieved {saveRoll} saves!!")
               else:
                    deathState += 1
                    print(f"{self._name} has failed a save roll!!!")
               
               #Breaking the while loop if either state has been achieved 
               if saveRoll == 3:
                    self._enemyHp = 20 + self._enemyDp
                    return f"The {self._name} returns to combat with {self._enemyHp}HP"
               elif deathState == 3:
                    return f"The {self._name} has died"

#Creating bandit enemy type               
class Bandit(Enemy):

     #Creating name
     def __init__(self, name=None):
          super.__init__(name)
          if self._name == None:
               name = "Bandit"
     
     #Creating bandit attack pattern 
     def banditAtk(self):
          attack = random.randint(0,self._atk)
          return attack


#Creating wolf enemy type               
class Wolf(Enemy):

     #Creating name
     def __init__(self, name=None):
          super.__init__(name)
          if self._name == None:
               name = "Wolf"
     
     #Creating wolf attack pattern 
     def banditAtk(self):
          attack = random.randint(0,self._atk)
          return attack
          
     
