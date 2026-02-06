#Creaitng current game logic 
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon

class GameExe:
     
    def __init__(self):
        #Enabling the main dungeon 
        self.__dungeon = Dungeon.DungeonRooms()
        #Allowing for the class to manipulate the class instance
        self.__player = None 
        self.__inventory = None 

    def gameInitalisation(self):
        print("Welcome to the DungeonCrawl")
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
        playerWeapon = Player.Weapon(self.__player)
        self.__inventory = UserInventory.PlayerInventory(self.__player)

        playerWeapon.weaponStart()
        startingWeapon = input("Please select a weapon: ")
        print(self.__inventory.newWeapon(startingWeapon))
        print(playerWeapon.weaponDmg(startingWeapon))
        return
    
    def dungeonSequence(self):
        #Creating entrance to the dungeon 
        print("You have entered an ominous place")
        currentRoom = self.__dungeon.getPlayerStateRoom()
        nextRoom = self.__dungeon.next_room()
        print(currentRoom)
        
        #Checking what room type is presesnt in the processs
        if currentRoom == "Trap-room":
            trapRoom = Dungeon.TrapRoom.statusEffect()
            print(trapRoom)
            return nextRoom
        elif currentRoom == "Merchant-Room":
            merchantRoom = Dungeon.MerchantRoom.merchantStock(self.__player)
            print(merchantRoom)
            return nextRoom
        elif currentRoom == "Arena-Room":
            arenaRoom = Dungeon.ArenaRoom.battleArena()
            print(arenaRoom)
            return nextRoom
        #Will add additional bosses later into an randomly assorted list to select from
        elif currentRoom == "Boss-Room":
            orge = Enemy.Ogre()
            bossRoom = Dungeon.BossRoom.bossEncounter(orge.enemyName())
            return bossRoom
        
    
        






















