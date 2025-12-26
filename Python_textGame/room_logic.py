#Creating dungeon room type 
import random
import enemy_logic
from player_logic import PlayerClass
class DungeonRooms:

    #Naming the dungeon room type
    def __init__(self):
        self._roomType = ["Trap-room","Arena-room","Merchant-room","Rest-room","Mini-boss"]
        self._currentRooms = 0
        self._currentPlay = {"Trap-room"  : 0,
                             "Arena-room" : 0,
                             "Merchant-room" : 0,
                             "Rest-room" : 0,
                             "Mini-boss" : 0,
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
            self._currentRooms = random.randint(5,7)
        elif user_length == "medium":
            self._currentRooms = random.randint(7,10)
        elif user_length ==  "long":
            self._currentRooms = random.randint(10,15)
        
        for i in range(self._currentRooms):
            room = random.choice(self._roomType)
            self._currentPlay[room] += 1
            self._roomSequence.append(room)

        
        return self._roomSequence

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
        if "Trap-room" in self._currentPlay:
            print("You have entered a trapped room!\n " \
                  "Rolling saving dice to recieve a status effect!")
            
            #Creating a save roll from the trap room
            playerSaveRoll = random.randint(0, 20) + PlayerClass.getPlayerDp()
            
            #Creating a fail method for the trap-room (WIll update the win condition later!)
            if playerSaveRoll < PlayerClass.getPlayerDp(): 
                playerDamage = (PlayerClass.getPlayerDp - playerSaveRoll) *10
                PlayerClass.playerDamge(playerDamage)
                return f"You have recieved {playerDamage} from failing the trap-room!!!"
            else:
                return f"You have escaped the trap-room!!"

            







    