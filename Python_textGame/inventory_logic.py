import random

#Creating player inventory for merchant usage and proficeny bonuses
class PlayerInventory: 
    #Creating a player instant variable that can be passed when defining player actions and health 
    def __init__(self,player):
        self.__player = player 
        
        #Creating a dictonary for manipulation
        self._playerInventory = {"gold": 25,
                                 "weapon": None,
                                 "armor": None,
                                 "potion": None}
    
    #Gather gold from dead enemies
    def pickingGold(self):
        enemyGold = random.randint(2,10)
        self._playerInventory['gold'] += enemyGold
        return f"You gained {enemyGold}"

    #Updating the player inventory with a new weapon 
    def newWeapon(self, new_weapon):
        self._playerInventory["weapon"] = new_weapon
        return f'You have equipped {self._playerInventory.get("weapon")}'
    
    def usingPotion(self):
        #Looping through the dictionary to ensure its inside the player inventory
        potion_name = self._playerInventory.get("potion")

        #If the player potion is health
        if potion_name == "Health-potion":
            healPlayer = self.__player.playerHeal(20)
            self._playerInventory['potion'] = None
            return f"You used a health potion: {healPlayer}hp"
        else:
            return "No potions were found!"
    
    #Creating a purchasing function for the merchants room works
    def buyingItem(self):
        #An expandable list that can allow for the addition of more potions if desired
        potionList = {1: "health-potion",
                      2: "stamanina-Potion",
                      3: "magic-Potion"}
        selectItem = input("\nPlease select an potion(press E to exit): ").lower()
        selectPotion = None

        #Checking if the user applies interger for the potion instead
        if selectItem.isdigit():
            itemNumber = int(selectItem)
            #Uses the item function for the dictionary to display both keys and values
            for potionNumber, potionName in potionList.items():
                if potionNumber == itemNumber:
                    selectPotion = potionName
                    break 
            #If the integer doesn't return with a proper 
            if selectPotion == None:
                return "Input a proper integer!"
              
        elif selectItem in potionList.values():
            selectPotion = selectItem
        #If the player decides to leave the shop
        elif selectItem == "e":
            return f"You have left the shop!"
        else:
            return("Please select a proper option!")

        #Checking if the player already has a potion in their inventory
        if self._playerInventory.get("potion") is not None:
            return f"You already have {self._playerInventory.get("potion")} in your inventory!"
            
        #Ensuring that the player has sufficent gold, otherwise they are kicked out!
        elif self._playerInventory.get("gold") >= 25:
            self._playerInventory["potion"] = selectPotion
            self._playerInventory["gold"] -= 25
            return f'You have purchased {selectPotion}\n'
        else:
            print("You do not have enough gold!!")
            return "Come back to me once you have some coin!"
            

    #Creating a return value for the gold to be checked
    def gettingGold(self):
        return self._playerInventory.get("gold")
    








