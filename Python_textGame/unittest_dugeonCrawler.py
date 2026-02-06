#importing game logic and running curent unit-tests on functionality and gameplay
import player_logic as Player
import enemy_logic as Enemy 
import inventory_logic as UserInventory 
import room_logic as Dungeon
import unittest

#Creating user test cases
class GameComponents(unittest.TestCase):
    def setUp(self):
        self._currentPlayer = Player.PlayerClass("Jake","Human",40,"warrior")
        self._currentWeapon = Player.Weapon(self._currentPlayer)
        self._currentDungeon = Dungeon.DungeonRooms()
        self._playerInventory = UserInventory(self._currentPlayer)
        self._originalHp = 100 
        self._originalSp = 100 
        self._originalMp = 100


#Creating playertests
class playerTest(GameComponents):

    def playerClassAttributesTest(self):
        self._currentPlayer.playerBonusStats()
        self._currentPlayer.classAttributes()

        self.assertEqual(self._currentPlayer.getplayerHealth(), self._originalHp+60)
        self.assertEqual(self._currentPlayer.getplayerStamania(), self._originalSp-20)
        self.assertEqual(self._currentPlayer.getplayerMagic(), self._originalMp+20)

    def playerWeaponAtkTest(self):
        self._currentWeapon.weaponDmg("great-sword")
        self.assertEqual(self._currentWeapon.getWeaponSAtk(), 4)

#Creating inventoruTests 
class inventoryTest(GameComponents):

    def playerBuysPotionTest(self):

        #Ensuring that the player gold is sufficent enough to be subtracted from
        self._playerInventory.pickingGold("Bandit")
        self.assertEqual(self._playerInventory.gettingGold(), 50)
        self._playerInventory.buyingItem()
        
        #ensuring that player inventory gold has changed 
        self.assertEqual(self._playerInventory.gettingGold(), 0)


#Creating dungeon room testing 
class DugeonRoomTest(GameComponents):

    #Creating a test case for a short duration of the dungeon 
    def settingDungeonLengthShort(self):
        self._currentDungeon.select_length()

        self.assertGreaterEqual(self._currentDungeon.getCurrentRooms(),5)
        self.assertLessEqual(self._currentDungeon.getCurrentRooms(),7)
    
    def settingDungeonLengthLong(self):
        #Creating a long varation to ensure proper usage 
        self._currentDungeon.select_length()

        self.assertGreaterEqual(self._currentDungeon.getCurrentRooms(),10)
        self.assertLessEqual(self._currentDungeon.getCurrentRooms(),15)


if __name__ == "__main__":
    unittest.main()

    


        








    



        


        



