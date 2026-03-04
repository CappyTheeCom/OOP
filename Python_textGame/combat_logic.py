#Creating player combat
import random
import player_logic as Player
from room_logic import ArenaRoom as Arena
import inventory_logic as Inventory
from enemy_logic import Enemy 

class Combat:
    
    def __init__(self, player, weapon, enemy):
        self._player = player 
        self._playerWeapon = weapon
        self._enemy = enemy

    #Creating character hit chance
    def playerHitChance(self):
      for enemy in self._enemy:
          enemyDmgRoll = random.randint(0, 20)
          
          #If enemy damage is less than the armor class
          if enemyDmgRoll < self._player._dp:
               print("Eneemy has missed there hit!!!")
          #If enemy damage is greater than the armor class
          elif enemyDmgRoll > self._player._dp:
               #Enemy damage
               enemyDmg = enemy.getEnemyAtk()
               self._player._hp -= enemyDmg
               print(f"The enemy has landed a hit. You take {enemyDmg} damage!!")
          #If something else happens that is not met by the conditions
          else:
               print(f"An error has occurred!!")
    
    #Creating enemy defensive points and hit-chance
    def enemyHitChance(self):  
      for enemy in self._enemy:
          playerDmgRoll = random.randint(0, 20)
          enemyDefense = enemy.getEnemyDF()

          if playerDmgRoll < enemyDefense:
               playerDmg = 0 
               print(f"Player missed! {playerDmg}dmg to enemy!!!")
          elif playerDmgRoll > enemyDefense:
               playerDmg = self._playerWeapon.getWeaponAtk()
               enemy.hitEnemy(playerDmg)
               print(f"Player did {playerDmg}dmg to enemy!!!")

                   
                   


#Creating testing code
if __name__ == '__main__':

     def CombatTest():
          #Player creation for test
          playerCreation = Player.PlayerClass("Jake","human",21,"warrior")
          playerWeapon = Player.Weapon(playerCreation)
          playerInventory = Inventory.PlayerInventory(playerCreation)
          startingWeapon = "club"

          print(playerCreation.classAttributes())
          print(playerInventory.newWeapon(startingWeapon))
          print(playerWeapon.weaponDmgCheck(startingWeapon))


          #Arena initalisation
          startArena = Arena()
          startArena.battleArena()



          #Main combat loop
          while startArena.remainingEnemies() > 0:
               #Creating menu
               print("1. Attack\n" \
                     "2. Potion\n" \
                     "3. Retreat" \
                    )
               
               #Player selects what option they want to do
               playerChoice = int(input("Please select an option!: "))
               #Creating turn based combat
               if playerChoice == 1:
                    
                    #Initalising current combat between player and enemies 
                    commenceCombat = Combat(playerCreation,playerWeapon,startArena.enemiesInArena())

                    commenceCombat.enemyHitChance()
                    for enemy in startArena.enemiesInArena():
                        enemyDeath = enemy.enemyDeathState()

                        if enemyDeath is True:
                            startArena.enemyDeathRemoval()
                    
                    #Creating player hit-chance and whether the player dies
                    commenceCombat.playerHitChance()
                    if playerCreation.playerDeathState() is True:
                        break
                        

               elif playerChoice == 2:
                   playerInventory.usingPotion() 
     
     CombatTest()