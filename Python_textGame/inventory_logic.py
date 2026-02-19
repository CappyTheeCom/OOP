import enemy_logic as enemyInventory

#Creating player inventory for merchant usage and proficeny bonuses
class PlayerInventory: 
    #Creating a player instant variable that can be passed when defining player actions and health 
    def __init__(self,player):
        self.__player = player 
        
        #Creating a dictonary for manipulation
        self._playerInventory = {"gold": 0,
                                 "weapon": "None",
                                 "armor": "None",
                                 "potion": "None"}
    
    #Gather gold from dead enemies
    def pickingGold(self, name):
        
        #Checking for the bandit name
        if name == "Bandit":
            #Creating bandit class
            banditGold = enemyInventory.Bandit()
            self._playerInventory["gold"] += banditGold.enemyGold()
        #Checking for the wolf name
        elif name == "Wolf":
            #Creating wolf class 
            wolfGold = enemyInventory.Wolf()
            self._playerInventory["gold"] += wolfGold.enemyGold()

    #Updating the player inventory with a new weapon 
    def newWeapon(self, new_weapon):
        self._playerInventory["weapon"] = new_weapon
        return f'You have equipped {self._playerInventory.get("weapon")}'
    
    #Updating the player inventory with a new armor
    def newArmor(self, new_armor):
        self._playerInventory["armor"] = new_armor
        return f'You have equipped {self._playerInventory.get("armor")}'
    
    #Updating player potion slots
    def newPotion(self, new_potion):
        self._playerInventory["potion"] = new_potion
        return f'You have equipped {self._playerInventory.get("potion")}'
    
    def usingPotion(self):
        #Looping through the dictionary to ensure its inside the player inventory
        potion_name = self._playerInventory.get("potion")
            #If the player potion is health
        if potion_name == "Health-potion":
            self.__player.playerHeal(50)
            self._playerInventory.get("potion") == "None"
            return f"You used a health potion: {self.__player.playerHealth()}hp"
        return "No potions were found!"
    
    #Creating a purchasing function for the merchants room works
    def buyingItem(self):
        #An expandable list that can allow for the addition of more potions if desired
        potionList = ["health","stamania","magic"]
        selectItem = input("\nPlease select an potion(press E to exit): ").lower()

        #Checks if the potion is within the allocate list and removes the player gold 
        if selectItem in potionList:
            if self._playerInventory.get("gold") >= 50:
                self._playerInventory["potion"] = selectItem
                self._playerInventory["gold"] -= 50
                return f'You have purchased {self._playerInventory.get("potion")}\n'
            else:
                print("You do not have enough gold!!")
        elif selectItem == "e":
            return f"You have left the shop!"
        else:
            print("Please select a proper option!")

    #Creating a return value for the gold to be checked
    def gettingGold(self):
        return self._playerInventory.get("gold")






