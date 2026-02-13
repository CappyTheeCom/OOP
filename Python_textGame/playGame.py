#Creaitng current game logic 
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon
import combat_logic as Combat

class GameExe:
     
    def __init__(self):
        #Enabling the main dungeon 
        self.__dungeon = Dungeon.DungeonRooms()
        #Allowing for the class to manipulate the class instance
        self.__player = None 
        self.__inventory = None 
        self.__arena = None
        self.__playerWeapon = None

    def gameInitalisation(self):
        print("Welcome to the DungeonCrawl")
        self.__dungeon.select_length()
        print(f"You have been given {self.__dungeon.getCurrentRoomIndex()} rooms")
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
        print(self.__playerWeapon.weaponDmg(startingWeapon))
        return
    
    def dungeonSequence(self):
        #Creating entrance to the dungeon 
        print("You have entered an ominous place")
        currentRoom = self.__dungeon.getPlayerStateRoom()
        print(f"You have entered {currentRoom}")
        
        #Checking what room type is presesnt in the processs
        if "Trap-room" in currentRoom:
            trapRoom = Dungeon.TrapRoom()
            print(trapRoom.statusEffect())
        elif "Merchant-room" in currentRoom:
            merchantRoom = Dungeon.MerchantRoom()
            print(merchantRoom.merchantStock(self.__player))
        elif "Arena-room" in currentRoom:
            self.__arena = Dungeon.ArenaRoom()
            print(self.__arena.battleArena())

        return currentRoom


    #Creating a combat action sequence    
    def combatSequence(self):
        #Creating player input for what they want to do!
        print("1. Attack\n" \
              "2. Potion\n" \
              "3. Retreat" \
              )
        
        playerChoice = input(int("Please select an option!: "))

        #Menu selection
        if playerChoice == 1:
            commenceCombat = Combat.Combat(self.__player, self.__arena.enemiesInArena(), self.__playerWeapon)
            commenceCombat.enemyHitChance()
            commenceCombat.playerHitChance()
            return commenceCombat
        elif playerChoice == 2:
            return self.__inventory.usingPotion()
        else:
            return "There is no retreat :)"
        
    
    #Creaitng merchant options and purchasing
    def merchantPurchasing(self):
        print("You have entered a quesitonable mans lair\n"\
              "1. health potion\n" \
              "2. Stamania Potion\n"\
              "3. magic potion")

        self.__inventory.buyingItem()
        return "You give your thanks"
    

def main():

    #Setting up games dungeons
    gameInit = GameExe()
    gameInit.gameInitalisation()

    #Creating player initalisation 
    gameInit.playerCreation()
    gameInit.playerWeaponSelection()

    currentRoom = gameInit.dungeonSequence()

    if "Arena-room" in currentRoom: 
        gameInit.combatSequence()
    elif "Merchant-room" in currentRoom:
        gameInit.merchantPurchasing()

main()


        










        


           

            

        






















