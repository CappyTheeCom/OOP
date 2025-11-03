import unittest 
from Assigntment2 import AustralianUser, FemaleUser, Under18User

class TestAustralianUser(unittest.TestCase):
     def setUp(self):
          self.male_young = AustralianUser(19,"male")
          self.male_middle = AustralianUser(51,"male")
          self.male_old = AustralianUser(80, "male")

          self.female_young = FemaleUser(30, "female", False, False)
          self.female_middle = FemaleUser(51, "female", False, False)
          self.female_old = FemaleUser(80,"female",False,False)

          self.female_bFeeder = FemaleUser(25,"female", False,True)
          self.female_pregnant = FemaleUser(30,"female",True,False)

          self.minor_teen = Under18User(17, "male")
          self.minor_kid = Under18User(9, "male")
          self.minor_infant = Under18User(2, "male")

          self.minorfem_teen = Under18User(17, "female")
          self.minorfem_kid = Under18User(9, "female")
          self.minorfem_infant = Under18User(2,"female")


     
     def test_dairy(self):

          
          self.assertEqual(self.male_young.dairy_intake(), "Your recommended dairy intake 2.5 servings")
          self.assertEqual(self.male_old.dairy_intake(),"Your recommended dairy intake 3.5 servings")

          self.assertEqual(self.female_young.dairy_intake(),"Your recommended dairy intake 2.5 servings")
          self.assertEqual(self.female_middle.dairy_intake(),"Your recommended dairy intake 4 servings")

          self.assertEqual(self.minor_teen.dairy_intake(),"Your recommended dairy intake 3.5 servings")
          self.assertEqual(self.minor_kid.dairy_intake(),"Your recommended dairy intake 2.5 servings")
          self.assertEqual(self.minorfem_kid.dairy_intake(),"Your recommended dairy intake 3.5 servings")

     def test_veg(self):

          self.assertEqual(self.male_young.veg_intake(), "Your recommended vegetable intake 6 servings")
          self.assertEqual(self.male_middle.veg_intake(),"Your recommended vegetable intake 5.5 servings")
          self.assertEqual(self.male_old.veg_intake(),"Your recommended vegetable intake 5 servings")

          self.assertEqual(self.female_bFeeder.veg_intake(),"Your recommended vegetable intake 7.5 servings")
          self.assertEqual(self.female_middle.veg_intake(),"Your recommended vegetable intake 5 servings")

          self.assertEqual(self.minor_teen.veg_intake(),"Your recommended vegetable intake 5.5 servings")
          self.assertEqual(self.minor_kid.veg_intake(),"Your recommended vegetable intake 5 servings")
          self.assertEqual(self.minor_infant.veg_intake(),"Your recommended vegetable intake 2.5 servings")

          self.assertEqual(self.minorfem_teen.veg_intake(),"Your recommended vegetable intake 5 servings")
          self.assertEqual(self.minorfem_kid.veg_intake(),"Your recommended vegetable intake 5 servings")
          self.assertEqual(self.minorfem_infant.veg_intake(),"Your recommended vegetable intake 2.5 servings")

     def test_meat(self):
   
          self.assertEqual(self.male_young.meat_intake(), "Your recommended meat intake 3 servings")
          self.assertEqual(self.male_middle.meat_intake(), "Your recommended meat intake 2.5 servings")
          
          self.assertEqual(self.female_pregnant.meat_intake(),"Your recommended meat intake 3.5 servings")
          self.assertEqual(self.female_young.meat_intake(),"Your recommended meat intake 2.5 servings")
          self.assertEqual(self.female_old.meat_intake(),"Your recommended meat intake 2 servings")

          self.assertEqual(self.minor_teen.meat_intake(),"Your recommended meat intake 2.5 servings")
          self.assertEqual(self.minor_kid.meat_intake(),"Your recommended meat intake 2.5 servings")
          self.assertEqual(self.minor_infant.meat_intake(),"Your recommended meat intake 1 servings")

     def test_fruit(self):
          self.assertEqual(self.male_young.fruit_intake(), "Your recommended fruit intake 2 servings")
          self.assertEqual(self.minor_kid.fruit_intake(), "Your recommended fruit intake 2 servings")
          self.assertEqual(self.minor_infant.fruit_intake(), "Your recommended fruit intake 1 servings")

     def test_grain(self):
          self.assertEqual(self.male_young.grain_intake(), "Your recommended grain intake 6 servings")
          self.assertEqual(self.male_old.grain_intake(), "Your recommended grain intake 4.5 servings")

          self.assertEqual(self.female_young.grain_intake(), "Your recommended grain intake 2.5 servings")
          self.assertEqual(self.female_old.grain_intake(), "Your recommended grain intake 3.5 servings")

          self.assertEqual(self.minor_teen.grain_intake(),"Your recommended grain intake 7 servings")
          self.assertEqual(self.minor_kid.grain_intake(),"Your recommended grain intake 5 servings")
          self.assertEqual(self.minor_infant.grain_intake(),"Your recommended grain intake 4 servings")

          self.assertEqual(self.minorfem_teen.grain_intake(),"Your recommended grain intake 7 servings")
          self.assertEqual(self.minorfem_kid.grain_intake(),"Your recommended grain intake 4 servings")
          self.assertEqual(self.minorfem_infant.grain_intake(),"Your recommended grain intake 4 servings")

          
if __name__ == "__main__":
     unittest.main()



