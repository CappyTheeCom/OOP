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
        else:
            return "Please select a proper state!"
        
        for i in range(self._currentRooms):
            room = random.choice(self._roomType)
            self._currentPlay[room] += 1
            self._roomSequence.append(room)

        
        return self._roomSequence
    
    #Creating getter methods for protected instances
    def getDungeonIndex(self):
        return self._currentRoomIndex
    
    def getCurrentRoom(self):
        return self._currentRooms
    
    def getPlayerStateRoom(self):
        roomType = self._roomSequence[self._currentRooms - 1]
        return roomType

    def getDungeonRoomSequence(self):
        roomSequence = self._roomSequence
        return roomSequence
    
    #Creating player movement 
    def next_room(self):
        if self._currentRoomIndex < self._currentRooms - 1:
            self._currentRoomIndex += 1   
            return f"You have moved into the {self._currentRoomIndex} room!!"
        else:
            return f"You have reached the end!!"                    

#Creating room types 
class TrapRoom:
    
    def __init__(self, dungeon, player):
        self.__dungeon = dungeon
        self.__player = player
        

    #Creating a chance to cycle through whether the player recieves a debuff or buff by entering the room
    def statusEffect(self):
        currentRoomIndex = self.__dungeon.getDungeonIndex()
        dungeonSequence = self.__dungeon.getDungeonRoomSequence()
        player = self.__player

        #Chccking if trap rooms are inside the list and will play a message if its in the current room!!
        if currentRoomIndex < len(dungeonSequence):
                print("You have entered a trapped room!\n " \
                    "Rolling saving dice to recieve a status effect!")
                
                #Creating a save roll from the trap room
                playerSaveRoll = random.randint(0,29)
                
                trapRoll = random.randint(0,20)
                #Creating a fail method for the trap-room (WIll update the win condition later!)
                if playerSaveRoll < trapRoll :
                    trapDamageroll = random.randint(1,10) 
                    playerDamage = (player.getPlayerDp()- trapDamageroll * 2)
                    player.playerDamge(playerDamage)
                    return f"You have recieved {playerDamage} from failing the trap-room!!!"
                else:
                    return f"You have escaped the trap-room!!"
    

#Creating merchant room and purchasing items
class MerchantRoom:
    
    def __init__(self, dungeon, player):
        self.__dungeon = dungeon
        self.__player = player
        self.__merchantStock = ["Health-potion","Stamania-potion","Magic-potion"]

    #Merchant Merchandise
    def merchantStock(self):
     #Printing the available stock for the user
     print("My current items in stock: ")
     for items in self.__merchantStock:
        print(items, end=" ")

     self.__player.buyingItem()
     return "You are welcome for my service..."

#Creating arena room for the enemies to spawn and fight in
class ArenaRoom:

    def __init__(self):
        self.__totalEnemies = []
        self.__enemiesInCmb = None
        self.__remainingEnemies = 0

    def battleArena(self):
        #Creating a random amount of enemies to spawn into the battle
        enemyAmount = random.randint(1,5)
        banditEnemy = EnemyEncounter.Bandit()
        wolfEnemy = EnemyEncounter.Wolf()
        enemyType = random.choice([banditEnemy, wolfEnemy])
        
        #Communicating to the player about the amount of combatents
        print("You have entered an Arena, prepare to fight!!")
        for enemy in range (0,enemyAmount):
            self.__totalEnemies.append(enemyType)
        #Printing the list of enemies that have appeared with string emagic method
        for enemy in self.__totalEnemies:
            print(f"A {str(enemy)} has appeared!!!")
            self.__remainingEnemies += 1
        
        return "Combat commences"
        
    def enemyDeathRemoval(self):
        
        #Looping through the list of enemies and hitting all enemies from the different attack roles
        #Creating an copied list from the original list, allowing for the removal of enemies without accidently skipping [:]
        for death in self.__enemiesInCmb:
            
            if death.enemyDeathState() is True:
                self.__remainingEnemies -= 1
                self.__totalEnemies.remove(death)
                self.__enemiesInCmb.remove(death)
                print(f"{self.__remainingEnemies} enemies remain!")

        
    #Returning the enemys from the arena 
    def enemiesInArena(self):
        if self.__enemiesInCmb is None:
            self.__enemiesInCmb = self.__totalEnemies[:]
        return self.__enemiesInCmb
    
    def remainingEnemies(self):
        return self.__remainingEnemies


#Creating boss encounter
class BossRoom(DungeonRooms):
    
    def __init__(self):
        super().__init__()
    
    #Creating a simple boss room for the enemy
    def bossEncounter(self, boss):
        return f"You have encoutnered an {boss}"

        

    