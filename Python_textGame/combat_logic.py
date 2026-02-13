#Creating player combat
import random
from room_logic import ArenaRoom

class Combat:
    
    def __init__(self, player, weapon, enemy):
        self._player = player 
        self._playerWeapon = weapon
        self._enemy = enemy
        self._arena = ArenaRoom()

    #Creating character hit chance
    def playerHitChance(self,enemyAtk):
          enemyDmgRoll = random.randint(0, enemyAtk)
          
          #If enemy damage is less than the armor class
          if enemyDmgRoll <= self._player._dp:
               return "Eneemy has missed there hit!!!"
          #If enemy damage is greater than the armor class
          elif enemyDmgRoll > self._player._dp:
               #Enemy damage
               enemyDmg = random.randint(0, enemyAtk - self._player._dp)
               
               self._player._hp -= enemyDmg
               return f"The enemy has landed a hit. You take {enemyDmg} damage!!"
          #If something else happens that is not met by the conditions
          else:
               return f"An error has occurred!!"
    
    #Creating enemy defensive points and hit-chance
    def enemyHitChance(self, enemyDP):
          playerDmgRoll = random.randint(0, 20)
          enemyDefense = enemyDP

          if playerDmgRoll <= enemyDefense:
               playerDmg = 0 
               return f"Player did {playerDmg}dmg to enemy!!!"
          elif playerDmgRoll > enemyDefense:
               playerDmg = random.randint(0, self._playerWeapon._weaponAtk ) - enemyDefense
               self._enemy.hitEnemy(playerDmg)
               return f"Player did {playerDmg}dmg to enemy!!!"



         
         