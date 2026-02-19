#Creating player combat
import random

class Combat:
    
    def __init__(self, player, enemy, weapon):
        self._player = player 
        self._playerWeapon = weapon
        self._enemyList = enemy
        self._turn = []

    #Creating character hit chance
    def playerHitChance(self):
     for enemy in self._enemyList:
          enemyDmgRoll = random.randint(0, enemy._atk)
          
          #If enemy damage is less than the armor class
          if enemyDmgRoll <= self._player._dp:
               return "Eneemy has missed there hit!!!"
          #If enemy damage is greater than the armor class
          elif enemyDmgRoll > self._player._dp:
               #Enemy damage
               enemyDmg = random.randint(0, enemy._atk - self._player._dp)
               
               self._hp -= enemyDmg
               return f"The enemy has landed a hit. You take {enemyDmg} damage!!"
          #If something else happens that is not met by the conditions
          else:
               return f"An error has occurred!!"
    
    #Creating enemy defensive points and hit-chance
    def enemyHitChance(self):
          
      for enemy in self._enemyList:
          playerDmgRoll = random.randint(0, 20)
          enemyDefense = enemy.getEnemyDF()

          if playerDmgRoll <= enemyDefense:
               playerDmg = 0 
               print(f"Player did {playerDmg}dmg to enemy!!!")
          elif playerDmgRoll > enemyDefense:
               playerDmg = random.randint(0, self._playerWeapon._weaponAtk ) - enemyDefense
               enemy.hitEnemy(playerDmg)
               print(f"Player did {playerDmg}dmg to enemy!!!")



         
         