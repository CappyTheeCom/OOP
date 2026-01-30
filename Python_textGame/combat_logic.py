#Creating player combat
import random
from room_logic import ArenaRoom

class Combat:
    
    def __init__(self, player, weapon, enemy):
        self._player = player 
        self._playerWeapon = weapon
        self._enemy = enemy
        self._turn = []
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
               
               self._hp -= enemyDmg
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

    #Creating turn state combat 
    def turnStateCombat(self):
         currentTurns = [self._player]
         currentTotalEnemies = self._arena.enemiesInArena()
         enemy = self._enemy
         weaponHit = self._playerWeapon
         playerHit = self._player

         #Appends current enemies into the turn list 
         for enemies in currentTotalEnemies:
              currentTurns.append(enemies)
          
         while any(enemy.getEnemyHp() > 0 for enemy in currentTotalEnemies):
              for turns in currentTurns:
                 if turns is self._player:
                   #Enemy recieves damage from the player weapon atk chance
                   #Creating live enemies list
                   live_enemies = [enemy for enemy in currentTotalEnemies if enemy.getEnemyHp > 0]
                   
                   if live_enemies:
                       target = random.choice(live_enemies)
                       target.hitEnemy(weaponHit.getWeaponAtk())

                 else:
                   #Player recieves damage
                   playerHit.playerDamage(enemy.getEnemyAtk())
              
              currentTotalEnemies = [enemy for enemy in currentTotalEnemies if enemy.getEnemyHp() > 0]
              currentTurns = [self._player] + currentTotalEnemies
             
         self._arena.next_room()
         return "You beat the the remaining enemies"
              
                  

               
          

                   

              

          
          



         
         