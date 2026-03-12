#Creaitng current game logic 
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon
import combat_logic as ArenaCombat

class GameExe:
     
    def __init__(self):
        #Enabling the main dungeon 
        self.__dungeon = Dungeon.DungeonRooms()
        #Allowing for the class to manipulate the class instance
        self.__player = None 
        self.__inventory = None
        self.__playerWeapon = None

    def gameInitalisation(self):
        print("Welcome to the DungeonCrawl")
        self.__dungeon.select_length()
        print(f"You have been given {self.__dungeon.getCurrentRoom()} rooms")
        return


    def playerCreation(self):
        #Creating player instance and inventory 
        playerRace = input("Please select a race (\"Human\",\"Half-Elf\",\"Elf\",\"Orc\",\"Dwarf\"): ")
        playerName = input("Please enter your character name: ")
        playerAge = int(input("Enter your character age: "))
        playerClass = input("Pleas enter a class you would like to use (warrior, rogue, mage): ")
        self.__player = Player.PlayerClass(playerName,playerRace,playerAge,playerClass)

        #Displaying the player current player decisions and attributes
        print(self.__player.playAbleRace())
        print(self.__player.playerBonusStats())
        print(self.__player.classAttributes())
        return
    

    def playerWeaponSelection(self):
        #Choosing player weapon
        self.__playerWeapon = Player.Weapon(self.__player)
        self.__inventory = UserInventory.PlayerInventory(self.__player)

        self.__playerWeapon.weaponStart()
        startingWeapon = input("Please select a weapon: ")
        print(self.__inventory.newWeapon(startingWeapon))
        print(self.__playerWeapon.weaponDmgCheck(startingWeapon))
        return
    
    #Moving throughout the dungeon and the win condition 
    def dungeonSequence(self):
        #Creating entrance to the dungeon 
        movingRoom = self.__dungeon.next_room()

        if movingRoom == "Trap-room":
            print(self.trapSection())
        elif movingRoom == "Arena-room":
            print(self.combatSequence())
        elif movingRoom == "Merchant-room":
            print(self.merchantSection())


    #Creating a combat action sequence    
    def combatSequence(self):
          #Arena initalisation
          startArena = Dungeon.ArenaRoom()
          startArena.battleArena()

          #Main combat loop
          while startArena.remainingEnemies() > 0:
               #Creating menu
               print("1. Attack\n" \
                     "2. Potion\n" \
                     "3. Check-Stats" \
                    )
               
               #Player selects what option they want to do
               playerChoice = int(input("Please select an option!: "))
               #Creating turn based combat
               if playerChoice == 1:
                    
                    #Initalising current combat between player and enemies 
                    commenceCombat = ArenaCombat.Combat(self.__player,self.__playerWeapon,startArena.enemiesInArena())

          
                    for enemy in startArena.enemiesInArena():
                        enemyDeath = enemy.enemyDeathState()
                        commenceCombat.enemyHitChance() 

                        #Checking if the function returns true to allow for death removal
                        if enemyDeath is True:
                            startArena.enemyDeathRemoval()
                            self.__inventory.pickingGold()
                    
                    #Creating player hit-chance and whether the player dies
                    commenceCombat.playerHitChance()
                    if self.__player.playerDeathState() is True:
                        break
               #Player using health potions
               elif playerChoice == 2:
                   print(self.__inventory.usingPotion())

               #Checking current player stats
               elif playerChoice == 3:
                   print(self.__player.checkingPlayerStats())
                   print(f"Current gold: {self.__inventory.gettingGold()}")
        
          return 

    #Creating merchantRoom-selection
    def merchantSection(self):
        merchantStk= Dungeon.MerchantRoom()

        merchantStk.merchantStock()
        self.__inventory.buyingItem()
        return

    #Creaitng trap room section 
    def trapSection(self):
        trapRoom = Dungeon.TrapRoom(self.__player)
        
        print(trapRoom.statusEffect())
        return
    
    #Creaitng current room index and size of the room

    def getDungeonSize(self):
       gameSize = self.__dungeon.getDungeonIndex()
       return gameSize
    
    def getDungeonLength(self):
        gameSize = self.__dungeon.getCurrentRoom()
        return gameSize
    
    #Getting player health
    def getPlayerHealth(self):
        return self.__player.getPlayerHealth()

def main():

    #Setting up games dungeons
    gameInit = GameExe()
    gameInit.gameInitalisation()

    #Creating player initalisation 
    gameInit.playerCreation()
    gameInit.playerWeaponSelection()

    while gameInit.getDungeonSize() < gameInit.getDungeonLength():
        
        if gameInit.getPlayerHealth() > 0 :
            print(gameInit.dungeonSequence())
        
        else:
            print("Game-over!")
            break

main()


        










        


           

            

        






















