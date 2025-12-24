#Creating dungeon room type 
import random
import enemy_logic
import player_logic

class DungeonRooms:

    #Naming the dungeon room type
    def __init__(self):
        self._roomType = ["Trap-room","Arena-room","Merchant-room","Rest-Room","Mini-Boss"]
        self._currentPlay = []


    #Creating length of the dungeon 
    def select_length(self):
        #Asking for user dungeon length
        user_length = input("Please select a dungeon length (Short, Meduim, Long): ")
        
        #making user_length universal 
        user_length.lower()
        
        #Applying coniditional statements for each room length
        if user_length == "short":
            dungeon_rooms = random.randint(5,7)
            
            #for every randomly selected room, the corrosponding function will be applied in relation to said room 
            for rooms in range (1,dungeon_rooms+1):
                room_selection = random.choice(self._roomType)
                self._currentPlay.append(room_selection)
            else:
                self._currentPlay.append("Boss-room")
                return
                

        #Meduim sized room and selection
        elif user_length == "meduim":
            dungeon_rooms = random.randint(8,12)

            for rooms in range (1, dungeon_rooms+1):
                room_selection = random.choice(self._roomType)
                self._currentPlay.append(room_selection)
            else:
                self._currentPlay.append("Boss-room")
                return

        #Long sized room and selection
        elif user_length == "long":
            dungeon_rooms = random.randint(12, 16)

            for rooms in range (1, dungeon_rooms+1):
                room_selection = random.choice(self._roomType)
                self._currentPlay.append(room_selection)
            else:
                self._currentPlay.append("Boss-room")
                return
            

#Creating room types 
class TrapRoom(DungeonRooms):
    
    def __init__(self):
        super().__init__()

    #Creating a chance to cycle through whether the player recieves a debuff or buff by entering the room
    def statusEffect(self):

        if "Trap-room" in self._currentPlay:
            print("You have entered a trapped room!\n " \
                  "Roll saving dice to recieve a status effect!")






    