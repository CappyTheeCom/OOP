import random
import player_logic

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
        