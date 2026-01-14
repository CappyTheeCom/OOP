#Creating dungeon room type 
import random
import enemy_logic as EnemyEncounter
from player_logic import PlayerClass

class DungeonRooms:

    #Naming the dungeon room type
    def __init__(self):
        self._roomType = ["Trap-room","Arena-room","Merchant-room"]
        self._currentRooms = 0
        self._currentPlay = {"Trap-room"  : 0,
                             "Arena-room" : 0,
                             "Merchant-room" : 0,
                             "Boss-room": 1}
        self._roomSequence = []
        self._currentRoomIndex = 0


    #Creating length of the dungeon 
    def select_length(self):
        #Asking for user dungeon length
        user_length = input("Please select a dungeon length (Short, Medium, Long): ")
        
        #making user_length universal 
        user_length = user_length.lower()
        
        #Applying coniditional statements for each room length
        if user_length == "short":
            self._currentRooms += random.randint(5,7)
        elif user_length == "medium":
            self._currentRooms += random.randint(7,10)
        elif user_length ==  "long":
            self._currentRooms += random.randint(10,15)
        
        for i in range(self._currentRooms):
            room = random.choice(self._roomType)
            self._currentPlay[room] += 1
            self._roomSequence.append(room)

        
        return self._roomSequence
    
    def getCurrentRooms(self):
        return self._currentRooms

    #Creating player movement 
    def next_room(self):
        if self._currentRoomIndex < self._currentRooms - 1:
            self._currentRooms += 1   
            return f"You have moved into the {self._currentRoomIndex} room!!"
        else:
            return f"You have reached the end!!"                    

#Creating room types 
class TrapRoom(DungeonRooms):
    
    def __init__(self):
        super().__init__()

    #Creating a chance to cycle through whether the player recieves a debuff or buff by entering the room
    def statusEffect(self):
        #Chccking if trap rooms are inside the list and will play a message if its in the current room!!
        if self._roomSequence[self._currentRoomIndex] == "TrapRoom":
            print("You have entered a trapped room!\n " \
                  "Rolling saving dice to recieve a status effect!")
            
            #Creating a save roll from the trap room
            playerSaveRoll = random.randint(0, 20)
            
            #Creating a fail method for the trap-room (WIll update the win condition later!)
            if playerSaveRoll < PlayerClass.getPlayerDp(): 
                playerDamage = (PlayerClass.getPlayerDp - playerSaveRoll) *10
                PlayerClass.playerDamge(playerDamage)
                return f"You have recieved {playerDamage} from failing the trap-room!!!"
            else:
                return f"You have escaped the trap-room!!"
    

#Creating merchant room and purchasing items
class MerchantRoom(DungeonRooms):
    
    def __init__(self):
        super().__init__()
        self.__merchantStock = ["Health-potion","Stamania-potion","Magic-potion"]

    #Merchant Merchandise
    def merchantStock(self, inventory):
        #Printing the available stock for the user
        if self._roomSequence[self._currentRoomIndex] == "Merchant-room":
            print("My current items in stock: ")
            for items in self.__merchantStock:
                print(items, end=" ")

            inventory.buyingItem()
            return "You are welcome for my service..."

#Creating arena room for the enemies to spawn and fight in
class ArenaRoom(DungeonRooms):

    def __init__(self):
        super.__init__()

    def battleArena(self):
        #Creating a random amount of enemies to spawn into the battle
        enemyAmount = random.randint(1,5)
        enemyType = random.choice[EnemyEncounter.Bandit(),EnemyEncounter.Wolf]
        totalEnemies = []
        totalAmount = 0
        
        #Communicating to the player about the amount of combatents
        print("You have entered an combat Arena, prepare to fight!!")
        for enemy in enemyAmount:
            totalEnemies.append(enemyType)
        #Printing the list of enemies that have appeared
        for enemy in totalEnemies:
            print(f"A {enemy} has appeared!!!")
            totalAmount += 1
        
        if totalAmount == 0:
            return f"You hav cleared the room of enemies"


#Creating boss encounter
class BossRoom(DungeonRooms):
    
    def __init__(self):
        super.__init__()
    
    #Creating a simple boss room for the enemy
    def bossEncounter(self, boss):
        print(f"You have encoutnered an {boss}")
        presentEnemy = 1 

        if presentEnemy == 0:
            return f"You have defeated the {boss}!!"

        

    