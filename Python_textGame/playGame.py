#Creaitng current game logic 
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon

def main():
    while True:
        #Creating weapons lists
        #Creating player dungeon size and allocating player name, race and class
        print("Welcome to the DungeonCrawl")
        Dungeon.DungeonRooms.select_length()
        print(f"You have been given {Dungeon.DungeonRooms.getCurrentRooms()} rooms")

        #Creating player instance
        playerRace = input("Please select a race (\"Human\",\"Half-Elf\",\"Elf\",\"Orc\",\"Dwarf\"): ")
        playerName = input("Please enter your character name: ")
        playerAge = int(input("Enter your character age: "))
        currentPlayer = Player.Player(playerName,playerRace,playerAge) 

        #Checking if the player race is correct
        currentPlayer.selectPlayerName() 
        currentPlayer.playAbleRace()
        currentPlayer.playerBonusStats()

        #Choosing player class
        playerClass = input("Pleas enter a class you would like to use (warrior, rogue, mage): ")
        currentClass = Player.PlayerClass(playerClass)
        currentClass.classAttributes()

        #Choosing player weapon
        playerWeapon = Player.Weapon(currentClass)
        playerInventory = UserInventory.PlayerInventory(playerWeapon)

        playerWeapon.weaponStart()
        startingWeapon = input("Please select a weapon")










