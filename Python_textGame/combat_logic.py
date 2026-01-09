#Creating player combat
import player_logic as Player 
import enemy_logic as Enemy
import random

class Combat:
    
    def __init__(self, player, enemy,weapon):
        self._player = player 
        self._playerWeapon = weapon
        self._enemy = enemy

    #Creating character hit chance
    def playerDefense(self):
          enemyDmgRoll = random.randint(0,self._enemy._atk)
          
          #If enemy damage is less than the armor class
          if enemyDmgRoll <= self._player._dp:
               return "Eneemy has missed there hit!!!"
          #If enemy damage is greater than the armor class
          elif enemyDmgRoll > self._player._dp:
               #Enemy damage
               enemyDmg = random.randint(0, self._enemy._atk - self._player._dp)
               
               self._hp -= enemyDmg
               return f"The enemy has landed a hit. You take {enemyDmg} damage!!"
          #If something else happens that is not met by the conditions
          else:
               return f"An error has occurred!!"
    
    #Creating enemy defensive points
    def enemyDF(self):
          playerDmgRoll = random.randint(0)

          if playerDmgRoll <= self._enemy._enemyDp:
               playerDmg = 0 
               return f"Player did {playerDmg}dmg to enemy!!!"
          elif playerDmgRoll > self._enemy._enemyDp:
               playerDmg = random.randint(0, self._playerWeapon._weaponAtk ) - self._enemy._enemyDp
               return f"Player did {playerDmg}dmg to enemy!!!"
          