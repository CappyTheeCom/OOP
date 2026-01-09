#Creaitng current game logic 
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon

def main():
    while True:
        #Creating player dungeon size and allocating player name, race and class
        print("Welcome to the DungeonCrawl")
        gameStart = Dungeon.DungeonRooms()
        gameStart.select_length()
        print(f"You have been given {gameStart.getCurrentRooms()} rooms")

        #Creating player instance
        playerRace = input("Please select a race (\"Human\",\"Half-Elf\",\"Elf\",\"Orc\",\"Dwarf\"): ")
        playerName = input("Please enter your character name: ")
        playerAge = int(input("Enter your character age: "))
        playerClass = input("Pleas enter a class you would like to use (warrior, rogue, mage): ")
        currentPlayer = Player.PlayerClass(playerName,playerRace,playerAge,playerClass)
        print(currentPlayer.playAbleRace())
        print(currentPlayer.playerBonusStats())
        print(currentPlayer.classAttributes())

        #Choosing player weapon
        playerWeapon = Player.Weapon(currentPlayer)
        playerInventory = UserInventory.PlayerInventory(currentPlayer)

        playerWeapon.weaponStart()
        startingWeapon = input("Please select a weapon: ")
        print(playerWeapon.weaponDmg(startingWeapon))
        print(playerInventory.newWeapon(startingWeapon))
        break

main()


















