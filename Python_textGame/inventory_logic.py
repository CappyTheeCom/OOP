import enemy_logic

#Creating player inventory for merchant usage and proficeny bonuses
class PlayerInventory: 
    #Checking for current armor, weapon and gold usage
    def __init__(self, weapon, armor, potion, gold):
        self._weapon = weapon
        self._armor =  armor 
        self._potion = potion
        self._gold = gold 
        
        #Creating a dictonary for manipulation
        self.player_inventory = {"gold": self._gold,
                                 "weapon-equipped": self._weapon,
                                 "armor-equipped": self._armor,
                                 "potion-equipped": self._potion}

    
   