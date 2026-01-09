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
        self._originalHp = 100 
        self._originalSp = 100 
        self._originalMp = 100


#Creating playertests
class playerTest(GameComponents):

    def playerClassAttributesTest(self):
        self._currentPlayer.playerBonusStats()
        self._currentPlayer.classAttributes()

        self.assertEqual(self._currentPlayer.getplayerHealth(), self._originalHp+60)
        self.assertEqual(self._currentPlayer.getplayerStamania, self._originalSp-20)
        self.assertEqual(self._currentPlayer.getplayerMagic(), self._originalMp+20)

    def playerWeaponAtkTest(self):
        self._currentWeapon.weaponDmg()

        


        



