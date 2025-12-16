import random

#Making enemy template
class Enenmy:
     def __init__(self):
          self._enemyHp = 100 
          self._enemyDp = 10 
          self._atk = 15 
    
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
               print("Enemy is in dying state!!!")

          while True: 

               #Creating condiitonal statement for the save state 
               if saveRoll >= self._enemyDp:
                    saveState += 1 
                    print(f"Enemy has achieved {saveRoll} saves!!")
               else:
                    deathState += 1
                    print("Enemy has failed a save roll!!!")
               
               #Breaking the while loop if either state has been achieved 
               if saveRoll == 3:
                    self._enemyHp = 20 + self._enemyDp
                    return f"The Enemy returns to combat with {self._enemyHp}HP"
               elif deathState == 3:
                    return "The enemy has died"

